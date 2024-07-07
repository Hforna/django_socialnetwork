from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.

def home(request):
    posts = Post.objects.all()
    if 'search_query' in request.GET:
        search_query = request.GET["search_query"]
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    context = {'posts': posts}

    return render(request, 'instamain/home.html', context=context)


