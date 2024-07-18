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


# Create your views here.

class SignUp(View):
    def get(self, request):
        if request.session.get("before_in_create_page", False):
            get_data_user_form = request.session.get("get_data_form", None)
            form = FormUser(get_data_user_form)
            request.session["before_in_create_page"] = False
        else:
            form = FormUser()
        return render(request, "accounts/signup.html", context={'form': form})


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
        return redirect("/accounts/login")
    return redirect("/accounts/signup")

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