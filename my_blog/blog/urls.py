from django.urls import path
from .views import home, about 
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )

urlpatterns = [
    path('about/', about, name="blog-about"),
    # path('', home, name="blog-home"),
    path('', PostListView.as_view(), name="blog-home"),
    path('userlist/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
]
