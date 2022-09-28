from django.urls import path
from .views import home, about

urlpatterns = [
    path('about/', about, name="blog-about"),
    path('', home, name="blog-home"),
]
