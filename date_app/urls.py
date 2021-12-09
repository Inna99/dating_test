from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter, DynamicRoute, Route

# from . import views
from date_app.views import UserViewSet

urlpatterns = [
    path("client/create", UserViewSet.as_view({"post": "create"}, permission_classes=[AllowAny])),
    path("list", UserViewSet.as_view({"get": "list"})),
    path("client/<int:id>/match", UserViewSet.as_view({"get": "match"})),
]
# class CustomRouter(DefaultRouter):
#     """
#     A router for read-only APIs, which doesn't use trailing slashes.
#     """
#     routes = [
#         # List route.
#         Route(
#             url=r'^{prefix}/create{trailing_slash}$',
#             mapping={
#                 'post': 'create'
#             },
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/list{trailing_slash}$',
#             mapping={
#                 'get': 'list',
#             },
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         # Dynamically generated list routes. Generated using
#         # @action(detail=False) decorator on methods of the viewset.
#         DynamicRoute(
#             url=r'^{prefix}/{url_path}{trailing_slash}$',
#             name='{basename}-{url_name}',
#             detail=False,
#             initkwargs={}
#         ),
#         # Detail route.
#         Route(
#             url=r'^{prefix}/{lookup}{trailing_slash}$',
#             mapping={
#                 'get': 'retrieve',
#                 'put': 'update',
#                 'patch': 'partial_update',
#                 'delete': 'destroy'
#             },
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Instance'}
#         ),
#         # Dynamically generated detail routes. Generated using
#         # @action(detail=True) decorator on methods of the viewset.
#         DynamicRoute(
#             url=r'^{prefix}/{lookup}/{url_path}{trailing_slash}$',
#             name='{basename}-{url_name}',
#             detail=True,
#             initkwargs={}
#         ),
#     ]
#
#
# router = CustomRouter()
# router.register('clients', UserViewSet)
