from . import views
from django.urls import path

urlpatterns = [
    path('register', views.UserRegistration.as_view()),
    path('login', views.UserLogin.as_view()),
    path('profile', views.UserProfile.as_view()),
    path('change-password', views.UserChangePassword.as_view())
]
