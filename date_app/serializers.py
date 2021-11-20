from rest_framework import serializers

from date_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["gender", "last_name", "first_name"]
        fields = '__all__'
