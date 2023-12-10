from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from . import forms
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    # form = forms.RegisterForm()
    # form = forms.RegisterForm(request.POST or None)

    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                messages.warning(request, 'Account created successfully')
                messages.error(request, 'Account created successfully')
                messages.info(request, 'Account created successfully')
                # form.save(commit=False)
                form.save()
                print(form.cleaned_data)
                # form = forms.RegisterForm()
        else:
            form = forms.RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                # checking username and password correct or not and also checking whether the user is in the database or not
                user = authenticate(username=username, password=password)
                if user is not None:  # if user is in the database
                    login(request, user)
                    # return render(request, 'home.html')
                    return redirect('profile')  # redirect to profile page
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user.username})
    else:
        return redirect('login')


# change user data
# def profile(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = forms.ChangeUserData(request.POST, instance=request.user)
#             if form.is_valid():
#                 messages.success(
#                     request, 'Your user data was successfully updated.')
#                 form.save()
#         else:
#             form = forms.ChangeUserData(instance=request.user)
#         return render(request, 'profile.html', {'form': form})
#     else:
#         return redirect('profile')


def logout_view(request):
    logout(request)
    # Add any additional logic here
    # return render(request, 'logout.html')
    return redirect('login')

# password change


def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # form = PasswordChangeForm(request.user, request.POST)
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important! Update the password hash
                # messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            # form = PasswordChangeForm(request.user)
            form = PasswordChangeForm(user=request.user)
        return render(request, 'password_change.html', {'form': form})
    else:
        return redirect('login')

def password_change_without_old_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important! Update the password hash
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'password_change.html', {'form': form})


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Your user data was successfully updated.')
                form.save()
                return redirect('profile')
        else:
            form = forms.ChangeUserData(instance=request.user)
        return render(request, 'change_user_data.html', {'form': form})
    else:
        return redirect('profile')
