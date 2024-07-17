from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from profiles.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        second_password = request.POST.get("second_password")
        if password == second_password:
            user_create = User.objects.create_user(username=username, password=password, email=email)
            user_create.save()
            messages.success(request, "Account created with success")
            return redirect("login")
        else:
            messages.error(request, "The passwords should be equal")
    
    return render(request, "accounts/signup.html")

def login_page(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        uss = User.objects.get(email=email)
        userr = authenticate(request, username=uss.username, password=password)
        if userr is not None:
            login(request, userr)
            return redirect("/")
        else:
            messages.error(request, "Email or password is wrong")

    
    return render(request, "accounts/login.html")

@login_required(login_url="/accounts/login", redirect_field_name="next")
def logouts(request):
    logout(request)
    return redirect("/accounts/login")