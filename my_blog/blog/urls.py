from django.urls import path
from .views import home, about 
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView
                    )

urlpatterns = [
    path('about/', about, name="blog-about"),
    # path('', home, name="blog-home"),
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
]
