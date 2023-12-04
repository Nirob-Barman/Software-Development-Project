from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('delete/<int:roll>', views.delete_student, name='deleteStudent'),
]