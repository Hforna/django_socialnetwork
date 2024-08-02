from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("/signup", SignUp.as_view(), name="sign_up"),
    path("/login", login_page, name="login"),
    path("/logout", logouts, name="logout"),
    path("/create_user", create_user, name="create_user"),
    path("/email_reset_password", email_reset_password, name="email_reset_password"),
    path("/verify_email", verify_email, name="verify_email"),
    path("/reset_password", reset_password, name="reset_password"),
    # Api endpoints
    path("/user-api", UserViewApi.as_view({"get": "list"})),
    path("/user-api/<int:pk>", UserViewApi.as_view({"get": "list"}), name="get_user"),
    path("/profile-api", ProfileViewApi.as_view({"get": "list"}), name="get-profiles"),
    path("/profile-api/<int:pk>", ProfileViewApi.as_view({"get": "list"}), name="get-profile"),
]
