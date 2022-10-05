from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# MVT - MVC
# register oldal
# 
# Create your views here.
# 1. létrehoztam a model-t -> az adatbázis része a fejlesztésnek
# 2. html
# 3. view, ami rendereli a html file-unkat
# 4. login endpoint, URL

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created! You are able to login!")
            return redirect('login')

    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context=context)