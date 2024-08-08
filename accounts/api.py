from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from profiles.models import Profile
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnProfile, IsOwnUser, IsOwnPost
from instamain.models import Post
from rest_framework.response import Response
from rest_framework import status



class PaginationUser(PageNumberPagination):
    page_size = 6

class UserViewApi(ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PaginationUser

    def get_permissions(self):
        if self.request.method in ["PATH", "PUT", "DELETE"]:
            return [IsOwnUser(), ]
        return super().get_permissions()

class ProfileViewApi(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ["PATCH", "PUT", "DELETE"]:
            return [IsOwnProfile(), ]
        return super().get_permissions()

    def get_queryset(self):
        sp = super().get_queryset()
        if sp.filter(pk=self.kwargs.get("pk")).filter(private_account=True).exists():
            return "This account is private"
        else:
            print(self.request.user)
            return sp

class PostViewApi(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []
    pagination_class = PaginationUser


    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsOwnPost(), ]
        return super().get_permissions()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile_post=Profile.objects.get(user_profile=self.request.user))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        profile = Profile.objects.get(user_profile=self.request.user)
        
        return Post.objects.filter(profile_post=profile)