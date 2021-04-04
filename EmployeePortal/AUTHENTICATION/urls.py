from django.urls import path
from .views import signupView

urlpatterns = [
    path('signup/', signupView, name='signup'),
    ]