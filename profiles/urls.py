from django.urls import path
from .views import *

urlpatterns = [
    path("/<str:profileuser>", profile_page, name="profile_page"),
    path("/posts_profile/add_post", add_post, name="add_post"),
    path("/posts_profile/delete_post/<int:pk>", delete_post, name="delete_post"),
    path("/posts_profile/edit_profile/<str:profileuser>", edit_profile, name="edit_profile")
]