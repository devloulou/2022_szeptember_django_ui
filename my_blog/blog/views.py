from django.shortcuts import render, get_object_or_404
from .models import PostsModel
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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

# a model-t és a template-et meg kell adni 
class PostListView(ListView):
    model = PostsModel
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = PostsModel
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        # user_obj = User.objects.get(username=self.kwargs.get('username'))
        user_obj = get_object_or_404(User, username=self.kwargs.get('username'))
        data = PostsModel.objects.filter(author=user_obj).order_by('-date_posted')       
        return data
        

class PostDetailView(DetailView):
    model = PostsModel
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostsModel
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostsModel
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostsModel
    template_name = 'blog/post_delete.html'
    success_url = "/"


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# mixins