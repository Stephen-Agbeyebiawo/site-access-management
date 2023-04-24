from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "sites/login.html", {
        "message":"Ener Username and Password"
    })

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return render(request, "sites/login.html", {
            "message":"Invalid Credentials"
        })

def logout_func(request):
    logout(request)
    return render(request, "sites/login.html", {
        "message":"Successfully Logged Out"
    })

def dashboard(request):
    return render(request, "dashboard/dashboard.html")