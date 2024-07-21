from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from profiles.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from .forms import FormUser
from django.http import Http404, HttpResponse
from profiles.models import Profile
from django.core.mail import send_mail
from core import settings
import random

# Create your views here.

class SignUp(View):
    def get(self, request):
        if not request.user.is_authenticated:
            if request.session.get("before_in_create_page", False):
                get_data_user_form = request.session.get("get_data_form", None)
                form = FormUser(get_data_user_form)
                request.session["before_in_create_page"] = False
            else:
                form = FormUser()
            return render(request, "accounts/signup.html", context={'form': form})
        else:
            return redirect("/")


def create_user(request):
    if request.method != "POST":
        return Http404
    
    form = FormUser(request.POST)
    request.session["get_data_form"] = request.POST
    request.session["before_in_create_page"] = True
    if form.is_valid():
        post = form.save(commit=False)
        post.set_password(post.password)
        post.save()
        request.session["get_data_form"] = None
        request.session["before_in_create_page"] = False
        messages.success(request, "Account created with success")
        return redirect("/accounts/login")
    return redirect("/accounts/signup")

def login_page(request):
    if not request.user.is_authenticated:
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
    else:
        return redirect("/")

    
    return render(request, "accounts/login.html")

def email_reset_password(request):
    if request.method == "POST":
        email = request.POST["email"].strip()
        request.session["code_to_reset"] = random.randint(234651, 498756)
        request.session["email_user"] = email
        code = request.session["code_to_reset"]
        if User.objects.filter(email=email).exists():
            send_mail(
                "Reset your password",
                f"Your verification code is: {code}",
                settings.EMAIL_HOST_USER,
                [f"{email}"]
            )
            return redirect("/accounts/verify_email")
        else:
            messages.error(request, "Invalid email")
            return redirect("/accounts/email_reset_password")
    
    return render(request, "accounts/email_reset_password.html")

def verify_email(request):
    if request.method == "POST":
        user_code_input = request.POST["security-code"].strip()
        stored_code = request.session.get("code_to_reset", "")

        try:
            stored_code = int(stored_code) 
        except ValueError:
            messages.error(request, "There was an error with the security code. Please try again.")
            return redirect("/accounts/verify_email")

        if user_code_input.isdigit() and int(user_code_input) == stored_code:
            return redirect("/accounts/reset_password")
        else:
            print(f"Expected code: {stored_code}") 
            print(f"User input: {user_code_input}")
            messages.error(request, "The code is incorrect")
            return redirect("/accounts/verify_email")

    return render(request, "accounts/verify_email.html")

def reset_password(request):    
    email = request.session["email_user"].strip()
    user = User.objects.get(email=email)
    if request.method == "POST":
        password1 = request.POST["new-password"].strip()
        password2 = request.POST["confirm-password"].strip()
        if password1 == password2:
            user.set_password(password1)
            user.save()
            messages.success(request, "Your password has been reseted")
            return redirect("/accounts/login")
        else:
            messages.error("The passwords must be equal") 
            return redirect("/accounts/reset_password")
        
    return render(request, "accounts/reset_password.html")

@login_required(login_url="/accounts/login", redirect_field_name="next")
def logouts(request):
    logout(request)
    request.session["anonymous"] = True
    return redirect("/accounts/login")