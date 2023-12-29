from django.shortcuts import render, redirect
from django.views.generic import FormView
from . forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class RegistrationView(FormView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/registration.html'

    def form_valid(self, form):
        user = form.save()
        print(user)
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class LoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        # return reverse_lazy('accounts:profile')
        return reverse_lazy('profile')
        # return reverse_lazy('home')


class LogoutView(LogoutView):
    def get_success_url(self):
        # if self.request.user.is_authenticated:
        #     logout(self.request)
        return reverse_lazy('home')


class UserProfileView(LoginRequiredMixin,View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        # return render(request, 'accounts/profile.html', {'form': form})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            return redirect('home')
        else:
            print(form.errors)
            # return render(request, 'accounts/profile.html', {'form': form})
        # return render(request, 'accounts/profile.html', {'form': form})
        return render(request, self.template_name, {'form': form})
