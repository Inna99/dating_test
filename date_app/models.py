from django.db import models


class User(models.Model):
    img = models.ImageField(upload_to='/article', height_field=100, width_field=100)
    gender = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(auto_now=True)
    date_created = models.DateTimeField(auto_created=True)

    def __str___(self):
        return f"{self.first_name} {self.last_name}"
