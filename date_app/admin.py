from django.contrib import admin

# Register your models here.
from date_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
#
# admin.site.register(User, UserAdmin)
