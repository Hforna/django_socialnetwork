from django.urls import path
from .views import *

urlpatterns = [
    path("/", ChatPage.as_view(), name="chat_page"),
    path("/send_message", send_message, name="send_message")
]
