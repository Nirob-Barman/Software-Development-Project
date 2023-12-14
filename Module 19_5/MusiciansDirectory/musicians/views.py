from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


from album.models import Album

from django.db.models import Q


from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView, DetailView

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        # musician = models.Musician.objects.get(email=request.user.email)
        # albums = Album.objects.filter(musician=musician)
        
        # musician = get_object_or_404(models.Musician, email=request.user.email)
        # albums = Album.objects.filter(musician=musician)
        # print(albums)

        musicians = models.Musician.objects.filter(email=request.user.email)
        if musicians.exists():
            musician = musicians.first()
            albums = Album.objects.filter(musician=musician)
            print(albums)

        # all_albums = Album.objects.all()
        # print(all_albums)
        # for a in all_albums:
        #     # print(a.album_name)
        #     print(a.musician.email)
        # return render(request, 'profile.html', {'albums': all_albums})
            return render(request, 'profile.html', {'albums': albums})
    else:
        return redirect('login')


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            form = forms.RegistrationForm()
        # return render(request, 'registration_form.html', {'form': form, 'title': 'Register', 'button_text': 'Register', 'button_class': 'btn-success'})
        return render(request, 'form.html', {'form': form, 'title': 'Registration', 'button_text': 'Register', 'button_class': 'btn-success'})
    else:
        return redirect('home')

# User registration using class-based view


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('login')
    success_message = 'Account created successfully'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        context['button_text'] = 'Register'
        context['button_class'] = 'btn-success'
        return context


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

# user login using class based view


class UserLoginView(SuccessMessageMixin,LoginView):
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, f'Welcome {form.get_user()}')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['button_text'] = 'Login'
        context['button_class'] = 'btn-primary'
        return context


def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, 'Logged out successfully')
        return response


def musician_list(request):
    musicians = models.Musician.objects.all()
    # print(musicians)
    sort_order = request.GET.get('sort_order')
    sort_field = request.GET.get('sort_field')

    if sort_order not in ['asc', 'desc']:
        sort_order = 'asc'

    if sort_field not in ['first_name', 'last_name', 'id', 'email', 'phone_number', 'instrument_type']:
        sort_field = 'first_name'

    if sort_order == 'asc':
        ordering = sort_field
    else:
        ordering = '-' + sort_field

    musicians = musicians.order_by(ordering)

    sort_field_options = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'id': 'ID',
        'email': 'Email',
        'phone_number': 'Phone Number',
        'instrument_type': 'Instrument Type',
    }

    # for field, label in sort_field_options.items():
    #     print(field,'-',label)

    search_form = forms.SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        # if query:
        #     musicians = musicians.filter(album_name__icontains=query)

        if query:
            musicians = musicians.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(instrument_type__icontains=query)
            )

    return render(request, 'musician_list.html', {'musicians': musicians, 'sort_field_options': sort_field_options, 'search_form': search_form})


def add_musician(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            musician_form = forms.MusicianForm(request.POST)
            if musician_form.is_valid():
                musician_form.save()
                return redirect('add_musician')
        else:
            musician_form = forms.MusicianForm()
        return render(request, 'add_musician.html', {'form': musician_form})
    else:
        return redirect('login')


# @method_decorator(login_required, name='dispatch')
class AddMusicianView(UserPassesTestMixin,CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        # Check if the user is authenticated
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        # Redirect to the login page if the user is not authenticated
        return redirect('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def edit_musician(request, musician_id):
    if request.user.is_authenticated:
        musician = models.Musician.objects.get(pk=musician_id)

        if request.method == 'POST':
            musician_form = forms.MusicianForm(request.POST, instance=musician)
            if musician_form.is_valid():
                musician_form.save()
                return redirect('home')
        else:
            musician_form = forms.MusicianForm(instance=musician)

        return render(request, 'add_musician.html', {'form': musician_form})
    else:
        return redirect('login')

class EditMusicianView(UserPassesTestMixin,UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'musician_id'

    def test_func(self):
        # Check if the user is authenticated
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        # Redirect to the login page if the user is not authenticated
        return redirect('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)