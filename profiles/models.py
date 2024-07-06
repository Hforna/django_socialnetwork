from django.db import models
from django.contrib.auth.models import User

class UserInfos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=20, default="")

class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=40, default="")
    profile_photo = models.ImageField(default="")
    description = models.CharField(max_length=600, default="")
    creator_profile = models.BooleanField(default=False)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    private_account = models.BooleanField(default=False)