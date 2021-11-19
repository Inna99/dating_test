from django.urls import path

from date_app import views

urlpatterns = [
    path("", views.ListTodoAPIView.as_view(), name="date_list"),
    path("create/", views.CreateTodoAPIView.as_view(), name="date_create"),
    path("update/<int:pk>/", views.UpdateTodoAPIView.as_view(), name="update_date"),
    path("delete/<int:pk>/", views.DeleteTodoAPIView.as_view(), name="delete_date"),
]
