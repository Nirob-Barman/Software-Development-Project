from django.shortcuts import render, redirect
from . import models
# Create your views here.


def home(request):
    student = models.Student.objects.all()
    # print(student)
    # contextData = {
    #     "student": student
    # }
    # return render(request, "home.html", contextData)
    return render(request, "home.html", {'data': student})


def delete_student(request, roll):
    # std = models.Student.objects.get(pk=roll)
    # print(std)
    # student = models.Student.objects.all()
    # print(student)
    # std.delete()
    # return render(request, "home.html", {'data': student})
    std = models.Student.objects.get(pk=roll).delete()
    return redirect('homePage')
