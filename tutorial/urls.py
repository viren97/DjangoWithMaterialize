from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("register/", views.register, name ="register"),
    path("login/", views.login_request, name = "login_request"),
    path('logout/', views.logout_request, name="logout_request"),
    path('<single_slug>', views.single_slug, name="single_slug"),
]
