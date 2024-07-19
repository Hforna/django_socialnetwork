from django.db import models
from django.contrib.auth.models import User
from profiles.models import *
import time

# Create your models here.



class Post(models.Model):
    profile_post = models.ForeignKey(Profile, related_name="user_post", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="medias/", default="")
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=600, default="")
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

class ListLikesPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile_liked = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Comment(models.Model):
    profile_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_commented = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=600)
    likes = models.IntegerField(default=0)

class ReplyComment(models.Model):
    profile_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    commented_in = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment = models.CharField(max_length=600)
    



