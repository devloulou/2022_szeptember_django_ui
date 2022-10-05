"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_registration.views import register as register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('register/', register_view, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name="logout"),
]


"""
1. server nevét - weboldalam nevét: 127.0.0.1:8000/about vagy localhost:8000 -> 
2. majd a project mappa urls.py-ből a megfelelő url-hez - ha include-van -
akkor az aktuális applikáció urls.py file-jában megkeresi az urlt és behelyettesíti
127.0.0.1:8000/
az ott megadott értéket
"""
