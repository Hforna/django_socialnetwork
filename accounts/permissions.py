from rest_framework.permissions import BasePermission
from profiles.models import Profile
from instamain.models import Post

class IsOwnProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_profile == request.user
        
    
class IsOwnUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username

class IsOwnPost(BasePermission):
    
    def has_permission(self, request, view):
        get_profile = Profile.objects.get(user_profile=request.user)
        get_profile_post = Post.objects.get(pk=view.kwargs.get("pk"))
        return get_profile == get_profile_post.profile_post
    
    
    