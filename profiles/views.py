from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, FollowersPerfil, FriendShip
from instamain.models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView
from django.views.generic import View
from django.db.models import Q
from .forms import FormPost
from django.http import HttpResponse


def profile_page(request, profileuser):
    profile = Profile.objects.get(user_profile=User.objects.get(username=profileuser))
    userr_profile = profile.user_profile
    posts = Post.objects.filter(profile_post=profile) if Post.objects.filter(profile_post=profile).exists() else None
    context = {"profile": profile, "posts": posts, "userr_profile": userr_profile}
    
    if request.user != userr_profile:
        if "follow_profile" in request.POST:
            profile_user_following = Profile.objects.get(user_profile=request.user)
            try:
                user_following = FollowersPerfil.objects.get(follower=profile, follower_user=request.user)
                user_following.delete()
                profile.followers -= 1
                profile.save()
                profile_user_following.following -= 1
                profile_user_following.save()
            except ObjectDoesNotExist:
                follow = FollowersPerfil.objects.create(follower=profile, follower_user=request.user)
                follow.save()
                profile.followers += 1
                profile.save()
                profile_user_following.following += 1
                profile_user_following.save()
            if FollowersPerfil.objects.filter(follower=profile_user_following, follower_user=profile.user_profile).exists():
                if not FriendShip.objects.filter(friend1=profile_user_following, friend2=profile).exists() or FriendShip.objects.filter(friend1=profile, friend2=profile_user_following).exists():
                    FriendShip.objects.create(friend1=profile_user_following, friend2=profile)
                else:
                    FriendShip.objects.filter(friend1=profile_user_following, friend2=profile).delete()

            return redirect('profile_page', profileuser=profileuser)

        profile.quantity_visits += 1
        profile.save()

    # Verifica se o usuário está seguindo o perfil
    is_following = FollowersPerfil.objects.filter(follower=profile, follower_user=request.user).exists()
    context["is_following"] = is_following
    
    return render(request, "profiles/profile_page.html", context=context)

def edit_profile(request, profileuser):
    profile = Profile.objects.get(user_profile=User.objects.get(username=request.user.username))
    if request.user == profile.user_profile:
        if request.method == "POST":
            profile_name = request.POST["profile_name"]
            description = request.POST["description"]
            profile.profile_name = profile_name
            profile.description = description
            try:
                profile_photo = request.FILES["profile_image"]
                profile.profile_photo = profile_photo
                profile.save()
            except MultiValueDictKeyError:
                profile.save()
            return redirect(f"/profile/{profileuser}")
    else:
        return redirect("/")

        
    return render(request, "profiles/edit_profile.html", context={"profile": profile})


class AddPost(View):
    form = FormPost()
    template_name = "profiles/add_post.html"

    def get(self, request):
        return render(request, "profiles/add_post.html", context={'form': self.form})
    
    def post(self, request):
        profile = Profile.objects.get(user_profile=request.user)
        form = FormPost(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.profile_post = profile
            post.save()

            return redirect(f"/profile/{profile.user_profile.username}")

        return render(request, "profiles/add_post.html", context={'form': self.form})

def create_post(request):
    form = FormPost(request.POST, request.FILES)



@csrf_exempt
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    profile = Profile.objects.get(user_profile=request.user)
    post.delete()
    return redirect(f"/profile/{profile.user_profile}")

class ShowProfiles(ListView):
    model = Profile
    template_name = "profiles/list_profiles.html"
    context_object_name = 'profiles'

class FriendPage(ListView):
    model = Profile
    template_name = "profiles/friends_page.html"
    context_object_name = 'profiles'

    def get_queryset(self):
        user_profilee = Profile.objects.get(user_profile=self.request.user)
        friends = FriendShip.objects.filter(Q(friend1=user_profilee) | Q(friend2=user_profilee))
        friend_list = []

        for friend in friends:
            if friend.friend1 != user_profilee:
                friend_list.append(friend.friend1)
            else:
                friend_list.append(friend.friend2)
        return friend_list
    