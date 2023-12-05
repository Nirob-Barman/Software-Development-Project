import datetime
from django import forms

class contactForm(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # message = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

    # Simple CharField
    name = forms.CharField(label='Your Name', initial="Nirob")

    # CharField with Textarea widget (default rows)
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

    # CharField with Textarea widget and custom attributes (e.g., 3 rows)
    additional_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        label='Additional Information'
    )

    # EmailField
    email = forms.EmailField(label='Your Email')

    # DateField
    BIRTH_YEAR_CHOICES = ['2021','2022','2023']
    
    birth_date = forms.DateField(
        label='Your Birth Date',
        initial=datetime.date.today,
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
        # widget=forms.SelectDateWidget(years=range(1900, 2023))
        # widget=forms.TextInput(attrs={'type': 'date'}),
        #  similar to SelectDateWidget but has a different appearance, resembling the date input used in the Django admin interface
        # widget=forms.AdminDateWidget(),
        # widget=forms.DateInput(attrs={'type': 'date'}),
    )

    # January 1, 2023, would be represented as '20230101'.
    # alternative_date = forms.DateField(
    #     widget=forms.NumberInput(attrs={'placeholder': 'YYYYMMDD'}),
    #     label='Alternative Date (YYYYMMDD)'
    # )

    # New DecimalField
    salary = forms.DecimalField(
        max_digits=10,  # Maximum number of digits, including decimal places
        decimal_places=2,  # Number of decimal places
        label='Your Salary'
    )

    # New ChoiceField with RadioSelect widget
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = forms.ChoiceField(
        choices=gender_choices,
        widget=forms.RadioSelect,
        label='Your Gender'
    )


    # New MultipleChoiceField
    fruit_choices = [
        ('apple', 'Apple'),
        ('banana', 'Banana'),
        ('orange', 'Orange'),
    ]
    
    favorite_fruits = forms.MultipleChoiceField(
        choices=fruit_choices,
        label='Favorite Fruits'
    )
    
    # New MultipleChoiceField with CheckboxSelectMultiple widget
    color_choices = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]
    
    favorite_colors = forms.MultipleChoiceField(
        choices=color_choices,
        widget=forms.CheckboxSelectMultiple,
        label='Favorite Colors'
    )


    # BooleanField (Checkbox)
    subscribe_to_newsletter = forms.BooleanField(
        required=False,
        initial=True,  # Default value (checked)
        label='Subscribe to Newsletter'
    )

