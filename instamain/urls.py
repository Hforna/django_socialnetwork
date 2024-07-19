from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path("post/<int:pk>", see_post, name="see_post")
]
