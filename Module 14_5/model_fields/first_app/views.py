from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    model = models.MyModel.objects.all()
    return render(request, 'home.html', {'contextData': model})
