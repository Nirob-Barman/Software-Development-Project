from django import forms
from django.core import validators

# widgets == field to html input


class contactForm(forms.Form):
    name = forms.CharField(label="Full Name", initial="Nirob Barman", help_text="Enter your name", required=False,
                           widget=forms.TextInput(attrs={'id': 'text_area', 'class': 'class1 class2', 'placeholder': 'Enter your name'}))
    # name = forms.CharField(label="Full Name", initial="Nirob Barman", help_text="Enter your name", required=False, widget=forms.Textarea)
    # email = forms.EmailField(label="Email", help_text="Enter your email", required=False)

    # name = forms.CharField(label="User Name")
    file = forms.FileField()

    # name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField(label="Weight")
    balance = forms.DecimalField()
    check = forms.BooleanField(label="Check")
    # birthday = forms.DateField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    # appointment = forms.DateTimeField()
    # appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    appointment = forms.CharField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
    # size = forms.ChoiceField(choices=CHOICES)
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [("P", "Pepperoni"), ("S", "Sausage"), ("C", "Cheese")]
    # pizza = forms.MultipleChoiceField(choices=MEAL)
    pizza = forms.MultipleChoiceField(
        choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.TextInput)

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Name is too short")
#     #     return valname

#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Email is not valid")
#     #     return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         # valname = self.cleaned_data['name']
#         # valemail = self.cleaned_data['email']

#         valname = cleaned_data.get('name')
#         valemail = cleaned_data.get('email')

#         # print(cleaned_data)

#         if len(valname) < 10:
#             raise forms.ValidationError("Name is too short")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Email is not valid")

#         # if valname and len(valname) < 10:
#         #     raise forms.ValidationError("Name is too short")

#         # if valemail and '.com' not in valemail:
#         #     raise forms.ValidationError("Email is not valid")

#         # return cleaned_data


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter at least 10 characters")


class StudentData(forms.Form):
    # name = forms.CharField(widget=forms.TextInput,validators =[validators.MinLengthValidator(10)])
    name = forms.CharField(widget=forms.TextInput, validators=[
                           validators.MinLengthValidator(10, message='Name is too short')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.EmailField(widget=forms.TextInput, validators=[
                             validators.EmailValidator(message='Email is not valid')])
    age = forms.IntegerField(validators=[
        # validators.MaxValueValidator(100, message='Age is too high'),
        # validators.MinValueValidator(0, message='Age cannot be negative')
        validators.MaxValueValidator(75, message='Age is too high'),
        validators.MinValueValidator(16, message='Age must be greater than 15')
    ])

    file = forms.FileField(validators=[validators.FileExtensionValidator(
        allowed_extensions=['jpg', 'png', 'pdf'])])



class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # cleaned_data = self.super().clean()
        cleaned_data = super().clean()
        
        # val_pass = self.cleaned_data['password']
        # val_confirm_pass = self.cleaned_data['confirm_password']
        # val_name = self.cleaned_data['name']

        val_pass = cleaned_data.get('password')
        val_confirm_pass = cleaned_data.get('confirm_password')
        val_name = cleaned_data.get('name')
        
        if val_pass != val_confirm_pass:
            raise forms.ValidationError("Password and Confirm Password does not match")

        if len(val_name) < 15:
            raise forms.ValidationError("Name is too short")

        # return cleaned_data

