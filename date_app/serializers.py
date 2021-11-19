from rest_framework import serializers

from date_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["gender", "email", "first_name"]
