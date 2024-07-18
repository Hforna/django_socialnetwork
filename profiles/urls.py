from django.urls import path
from .views import *

urlpatterns = [
    path("/<str:profileuser>", profile_page, name="profile_page"),
    path("/posts_profile/add_post", AddPost.as_view(), name="add_post"),
    path("/posts_profile/delete_post/<int:pk>", delete_post, name="delete_post"),
    path("/posts_profile/edit_profile/<str:profileuser>", edit_profile, name="edit_profile"),
    path("/pf/explore", ShowProfiles.as_view(), name="find_profiles"),
    path("/pf/friends", FriendPage.as_view(), name="friends")
]