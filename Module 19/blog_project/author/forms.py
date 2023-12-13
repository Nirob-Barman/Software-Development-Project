from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'
#         # fields = ['name', 'bio', 'phone_no']
#         # exclude = ['phone_no']
#     bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))

    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        fields = ['username', 'first_name', 'last_name', 'email']


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
