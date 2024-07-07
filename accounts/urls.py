from django.urls import path
from .views import *

urlpatterns = [
    path("/signup", sign_up, name="sign_up"),
    path("/login", login_page, name="login"),
    path("/logout", logouts, name="logout")
]
