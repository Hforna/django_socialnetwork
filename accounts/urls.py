from django.urls import path
from .views import *

urlpatterns = [
    path("/signup", SignUp.as_view(), name="sign_up"),
    path("/login", login_page, name="login"),
    path("/logout", logouts, name="logout"),
    path("/create_user", create_user, name="create_user"),
    path("/email_reset_password", email_reset_password, name="email_reset_password"),
    path("/verify_email", verify_email, name="verify_email"),
    path("/reset_password", reset_password, name="reset_password")
]
