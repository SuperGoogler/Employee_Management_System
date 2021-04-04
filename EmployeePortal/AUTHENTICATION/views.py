from django.shortcuts import render, redirect
from .forms import NewUserCreateForm
from django.contrib import messages
from  rest_framework import generics


# Create your views here.


def signupView(request):
    if request.method == 'POST':
        form = NewUserCreateForm(request.POST)
        if form.is_valid():
            form = NewUserCreateForm(request.POST)
            form.save()
            form.refresh_from_db()
            return redirect('authentication\\signup.html')
        else:
            messages.error(request, f'please check errors')
    else:
        form = NewUserCreateForm()
    return render(request, 'authentication\\signup.html', {'form': form})

