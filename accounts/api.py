from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from profiles.models import Profile

class PaginationUser(PageNumberPagination):
    page_size = 6

class UserViewApi(ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PaginationUser

class ProfileViewApi(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer