from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from profiles.models import Profile
from rest_framework import serializers
from instamain.models import Post

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["profile_name", "description", "profile_photo", "posts", "followers", "following", "private_account", "quantity_visits"]
    



class UserSerializer(ModelSerializer):
    profiles = serializers.HyperlinkedRelatedField(many=False, source="profile", read_only=False, queryset=Profile.objects.all(), view_name="get-profile-detail") 

    class Meta:
        model = User
        fields = ["username", "password", "email", "profiles"]

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ["profile_post", "images", "title", "description", "likes", "comments"]
        read_only_fields = ["profile_post"]
