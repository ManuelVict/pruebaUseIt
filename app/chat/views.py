from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    return redirect('/login.html ')

def register(request):
    return render(request, "/register.html")

def login(request):
    return render(request, "/login.html")

def logout(request):

    do_logout(request)
    return render(request, "/welcome.html")

