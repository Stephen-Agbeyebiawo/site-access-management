from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout_func, name="logout")
]