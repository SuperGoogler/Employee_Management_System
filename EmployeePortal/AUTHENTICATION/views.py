from django.shortcuts import render, redirect
from .forms import NewUserCreateForm
from django.contrib import messages
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from .serializers import RegistrationSerializers
from .models import NewEmployeeProfile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


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


class UserRegisterView(ListCreateAPIView):
    create_queryset = NewEmployeeProfile.objects.all()
    serializer_class = RegistrationSerializers
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.errors
            newUser = serializer.save()
            serializer = RegistrationSerializers(newUser)
            return Response(data={"status": "OK", "message": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(data={"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

