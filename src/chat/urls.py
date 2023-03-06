from django.contrib import admin
from django.urls import path, re_path

from . import views


urlpatterns = [
    # re_path("", views.index, name="index"),  # TODO: implement rooms
    # re_path("chat/", views.index, name="index"),
    # path("chat/<str:room_name>/", views.room, name="room"),

    path("", views.redirect_view),
    re_path("chat/", views.room, name="room"),
    re_path("register/", views.register_request, name="register"),
    re_path("login/", views.login_request, name="login"),
    re_path("logout/", views.logout_request, name="logout"),
]
