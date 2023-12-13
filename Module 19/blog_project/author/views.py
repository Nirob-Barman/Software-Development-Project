from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.urls import reverse
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.


# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             # author_form = forms.AuthorForm()
#             # return render(request, 'addAuthor.html', {'form': author_form})
#             # redirect('add_author')
#             return redirect('add_author')
#             # return redirect(reverse('add_author'))
#     else:
#         author_form = forms.AuthorForm()
#     # author_form = forms.AuthorForm()
#     return render(request, 'addAuthor.html', {'form': author_form})

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, 'Login successful')
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'Login'})

# user login using class based view
class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        # user = form.get_user()
        messages.success(self.request, 'Login successful')
        # login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def logout_view(request):
    logout(request)
    return redirect('user_login')

# implement logout view
class UserLogoutView(LogoutView):
    next_page = 'homePage'

@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    # print(data)
    return render(request, 'profile.html', {'data': data})

@login_required
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(
                    request, 'Your user data was successfully updated.')
                form.save()
                return redirect('profile')
        else:
            form = forms.ChangeUserData(instance=request.user)
        return render(request, 'update_profile.html', {'form': form, 'type': 'Profile'})
    else:
        return redirect('profile')


def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                # Important! Update the password hash
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'password_change.html', {'form': form, 'type': 'Password Change'})
    else:
        return redirect('login')
