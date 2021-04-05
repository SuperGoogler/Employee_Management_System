from django.urls import path
from .views import signupView, UserRegisterView


urlpatterns = [
    path('signup/', signupView, name='signup'),
    path('register/', UserRegisterView.as_view(), name='register'),
    ]