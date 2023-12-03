from django.shortcuts import render
from . forms import contactForm, StudentData, PasswordValidationProject

# Create your views here.

def home(request):
    return render(request, './first_app/home.html')


def about(request):
    # print(request.POST)
    if (request.method == 'POST'):
        # name = request.POST['username']
        # email = request.POST['email']
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        # print(name, email)
        return render(request, './first_app/about.html', {'name': name, 'email': email, 'select': select})
    else:
        # return render(request, './first_app/about.html', {'name': name, 'email': email, 'select': select})
        return render(request, './first_app/about.html')

    # return render(request, './first_app/about.html')


def submit_form(request):
    # # print(request.POST)
    # if(request.method == 'POST'):
    #     # name = request.POST['username']
    #     # email = request.POST['email']
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     # print(name, email)
    #     return render(request, './first_app/form.html', {'name': name, 'email': email})
    # else:
    #     return render(request, './first_app/form.html')

    return render(request, './first_app/form.html')

# def DjangoForm(request):
#     # form = contactForm()
#     form = contactForm(request.POST)
#     # print(form)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request, './first_app/django_form.html', {'form':form})


def DjangoForm(request):
    # form = contactForm()
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)

            print(form.cleaned_data)
            # return render(request, './first_app/django_form.html', {'form': form})
    else:
        form = contactForm()

    return render(request, './first_app/django_form.html', {'form': form})


def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()

    return render(request, './first_app/django_student_form.html', {'form': form})


def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()

    return render(request, './first_app/password_form_validation.html', {'form': form})
