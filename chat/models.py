from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatOneToOne(models.Model):
    user2 = models.ForeignKey(User, related_name="friend", on_delete=models.CASCADE)
    user1 = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    send_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=2560)
    user_sent = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_sent = models.ForeignKey(ChatOneToOne, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
