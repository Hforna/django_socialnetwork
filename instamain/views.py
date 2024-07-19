from django.shortcuts import render, redirect
from .models import Post, ListLikesPost, Comment
from django.db.models import Q
from profiles.models import Profile

# Create your views here.

def home(request):
    posts = Post.objects.all()
    posts.prefetch_related("profile_post")
    comments = Comment.objects.all()
    if 'search_query' in request.GET:
        search_query = request.GET["search_query"]
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    context = {'posts': posts, 'comments': comments}

    return render(request, 'instamain/home.html', context=context)

def see_post(request, pk):
    post = Post.objects.get(pk=pk)
    user_seeing = Profile.objects.get(user_profile=request.user)
    list_comments = []
    if Comment.objects.filter(post_commented=post).exists():
        for comment in Comment.objects.filter(post_commented=post):
            list_comments.append(comment) 

    context = {'post': post, 'list_comments': list_comments}
    if "like_post" in request.POST:
        if ListLikesPost.objects.filter(profile_liked=user_seeing, post=post).exists():
            post.likes -= 1
            ListLikesPost.objects.filter(profile_liked=user_seeing, post=post).first().delete()
        else:
            post.liked += 1
            liked = ListLikesPost.objects.create(profile_liked=user_seeing, post=post)
            liked.save()
    elif "comment_in_post" in request.POST:
        comment = request.POST["comment"]
        cr_comment = Comment.objects.create(profile_comment=user_seeing, post_commented=post, comment=comment)
        cr_comment.save()
        post.comments += 1
        return redirect(f"/post/{pk}")
    
    return render(request, "instamain/see_post.html", context=context)
