from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'required'}), max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'required'}), max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'required'}))
    password2 = forms.PasswordInput(attrs={'label': 'Confirm Password'})
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email']
        # fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email']
        # Customize the name of the form
        labels = {
            'username': 'New Username',
            'email': 'New Email',
            'first_name': 'New First Name',
            'last_name': 'New Last Name',
            # Add other fields as needed
        }
