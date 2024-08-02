from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from profiles.models import Profile
from rest_framework import serializers

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["profile_name", "description", "profile_photo", "posts", "followers", "following", "private_account", "quantity_visits"]
    



class UserSerializer(ModelSerializer):
    profiles = serializers.HyperlinkedRelatedField(many=False, source="profile", read_only=False, queryset=Profile.objects.all(), view_name="get-profile") 

    class Meta:
        model = User
        fields = ["username", "password", "email", "profiles"]