from django.db import models
from django.contrib.auth.models import User
from profiles.models import *
# Create your models here.



class Post(models.Model):
    profile_post = models.ForeignKey(Profile, on_delete=models.CASCADE)
    images = models.ImageField(default="")
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=600, default="")
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

class Comment(models.Model):
    profile_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_commented = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=600)
    likes = models.IntegerField(default=0)

class ReplyComment(models.Model):
    profile_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    commented_in = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment = models.CharField(max_length=600)
    



