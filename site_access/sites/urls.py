from . import views
from django.urls import path

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("dashboard", views.dashboard, name="dashboard")
]