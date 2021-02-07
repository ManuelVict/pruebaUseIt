from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.


def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def chat(request):
    return render(request, 'chat.html')

def salir(request):
    logout(request)
    return redirect('login')









