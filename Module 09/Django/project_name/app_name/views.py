from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("This is home page from app name")


def courses(request):
    return HttpResponse("This is courses page from app name")


def about(request):
    return HttpResponse("This is about page from app name")
