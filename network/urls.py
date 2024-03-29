
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.post, name="post"),
    path("user/<str:user_id>", views.profile, name="profile"),
    path("follow", views.follow, name="follow"),
    path("like/<str:post_id>", views.like, name="like"),
    path("post/<str:post_id>", views.post, name="post"),
]
