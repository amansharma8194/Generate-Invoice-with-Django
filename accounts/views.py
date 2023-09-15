from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def register_user(request):
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'User registered Successfully!')
            return redirect('/register/')
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form': form})



def login_user(request):
    if request.method=="POST":
        form = UserLogin(request, data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password=password)
            if user is None:
                messages.error(request, 'Incorrect Username or Password!')
            else:
                login(request, user)
                return redirect('/home/')
    else:
        form = UserLogin()
    return render(request, 'login_page.html', {'form': form})


