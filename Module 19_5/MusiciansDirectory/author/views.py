from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


from album.models import Album
# Create your views here.

def profile(request):
    data = Album.objects.filter(musician=request.user)
    print("Hi: ")
    print(data)
    print("Bye")
    return render(request, 'profile.html', {'data': data})
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegistraionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            form = forms.RegistraionForm()
        # return render(request, 'registration_form.html', {'form': form, 'title': 'Register', 'button_text': 'Register', 'button_class': 'btn-success'})
        return render(request, 'form.html', {'form': form, 'title': 'Registration', 'button_text': 'Register', 'button_class': 'btn-success'})
    else:
        return redirect('home')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome {username}')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password')
        else:
            form = AuthenticationForm()
        return render(request, 'form.html', {'form': form, 'title': 'Login', 'button_text': 'Login', 'button_class': 'btn-primary'})
    else:
        return redirect('home')


def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('home')