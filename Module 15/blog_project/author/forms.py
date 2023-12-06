from django import forms
from . models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['name', 'bio', 'phone_no']
        # exclude = ['phone_no']
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
