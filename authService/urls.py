from . import views
from django.urls import path

urlpatterns = [
    path('register', views.UserRegistration.as_view())
]
