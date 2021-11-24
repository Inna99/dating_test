# from django.shortcuts import render
from django.http import HttpRequest
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from date_app.models import User
from date_app.serializers import UserSerializer


class UserFilter(filters.FilterSet):
    name_in = filters.CharFilter(field_name="email")

    class Meta:
        model = User
        fields = ("gender", "first_name", "last_name")


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    # search_fields = ["id", "last_name"]
    # filterset_fields = ('gender', 'first_name', 'last_name')

    @action(detail=True, methods=["GET"], name="Get Highlight")
    def match(self, request, *args, **kwargs):
        #
        # print(args, kwargs[pk])
        request: HttpRequest
        # request.headers token -> from_user_id url -> to_user_id=kwargs[pk]
        # user:User
        # user.user_likes_set
        queryset = User.objects.filter(id__gt=12).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
