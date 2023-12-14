from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Musician


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))

    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        fields = ['username', 'first_name', 'last_name', 'email']


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'


class SearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Search musicians...'}))
