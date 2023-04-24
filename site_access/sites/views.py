from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "sites/login.html")

def dashboard(request):
    return render(request, "dashboard/dashboard.html")