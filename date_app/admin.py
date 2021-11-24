from django.contrib import admin

# Register your models here.
from date_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
