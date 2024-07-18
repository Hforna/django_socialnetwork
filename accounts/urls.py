from django.urls import path
from .views import *

urlpatterns = [
    path("/signup", SignUp.as_view(), name="sign_up"),
    path("/login", login_page, name="login"),
    path("/logout", logouts, name="logout"),
    path("/create_user", create_user, name="create_user")
]
