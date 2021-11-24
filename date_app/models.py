import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F
from django.db.models.functions import ACos, Cos, Radians, Sin

from script import watermark_with_photo


class User(AbstractUser):
    GENDER_CHOICES = [
        ("F", "female"),
        ("M", "male"),
    ]

    img = models.ImageField(blank=True, upload_to="users_img")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField("self", blank=True)

    def save(self, *args, **kwargs):
        if self.img:
            watermark_with_photo(
                self.img,
                f"media/users_img/{self.img}_watermarked.jpg",
                "watermark.jpg",
                position=(0, 0),
            )
            self.img = f"{self.img}_watermarked.jpg"
        # r = Path(s) file.php.jpg
        # r.basename
        return super().save(*args, **kwargs)

    def __str___(self):
        return f"{self.first_name} {self.last_name}"

    def range_filter(self, range_in_meters):
        # select count(*) as t
        distance = {
            "distance": 6367
            * ACos(
                Cos(Radians(self.latitude))
                * Cos(Radians(F("latitude")))
                * Cos(Radians(F("longitude")) - Radians(self.longitude))
                + Sin(Radians(self.latitude)) * Sin(Radians(F("latitude")))
            ),
        }
        qs = User.objects.annotate(**distance)
        delta = 2 * range_in_meters / 111.3
        qs = qs.filter(latitude__gte=self.latitude - delta)
        qs = qs.filter(latitude__lte=self.latitude + delta)
        qs = qs.filter(longitude__gte=self.longitude - delta)
        qs = qs.filter(longitude__lte=self.longitude + delta)
        qs = qs.filter(distance__lte=range_in_meters)

        return qs.all()


# class UserLikes(models.Model):
#     who = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name=)
#     whom = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
