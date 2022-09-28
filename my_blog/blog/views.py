from django.shortcuts import render
from .models import PostsModel
# Create your views here.
"""
MVC - MVT: Model View Template
"""
# function-based view
def home(request):
    posts = PostsModel.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html')