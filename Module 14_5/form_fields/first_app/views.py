from django.shortcuts import render
from . forms import contactForm

# Create your views here.


def home(request):
    return render(request, 'first_app/home.html')


def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # print(name, email, message)
    else:
        form = contactForm()
    return render(request, './first_app/django_form.html', {'form': form})
