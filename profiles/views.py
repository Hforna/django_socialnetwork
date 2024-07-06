from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

@login_required
def profile_page(request):
    user = User.objects.get(user=request.user)
    profile = Profile.objects.get(user_profile=user)
    
