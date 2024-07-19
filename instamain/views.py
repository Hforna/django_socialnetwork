from django.shortcuts import render
from .models import Post, ListLikesPost
from django.db.models import Q
from profiles.models import Profile

# Create your views here.

def home(request):
    posts = Post.objects.all()
    posts.prefetch_related("profile_post")
    if 'search_query' in request.GET:
        search_query = request.GET["search_query"]
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    context = {'posts': posts}

    return render(request, 'instamain/home.html', context=context)

def see_post(request, pk):
    post = Post.objects.get(pk=pk)
    user_seeing = Profile.objects.get(user_profile=request.user)
    if "like_post" in request.POST:
        if ListLikesPost.objects.filter(profile_liked=user_seeing, post=post).exists():
            post.likes -= 1
            ListLikesPost.objects.filter(profile_liked=user_seeing, post=post).first().delete()
        else:
            post.liked += 1
            liked = ListLikesPost.objects.create(profile_liked=user_seeing, post=post)
            liked.save()
    elif "comment_in_post" in request.POST:
        post.comments += 1
