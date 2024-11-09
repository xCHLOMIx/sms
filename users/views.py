from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import CustomUser
# Create your views here.

def registerView(request):
    error = ''
    if request.method == "POST":
        username = request.POST['username']
        password = make_password(request.POST['password'])

        if CustomUser.objects.filter(username = username).exists():
            error = 'Username already exists'

            return render(request, "users/register.html", { "error" : error })
        else:
            user = CustomUser(username = username, password = password)
            user.save()

        return redirect('login')


    return render(request, "users/register.html")

def loginView(request):
    error = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = "Invalid Credentials"
    
    return render(request, "users/login.html", { "error" : error})