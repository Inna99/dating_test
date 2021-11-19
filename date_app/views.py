from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from date_app.serializers import UserSerializer
from date_app.models import User


# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
