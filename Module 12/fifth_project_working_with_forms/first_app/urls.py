from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('form/', views.submit_form, name='formpage'),
    path('django_form/', views.DjangoForm, name='djangoform'),
    path('django_student_form/', views.StudentForm, name='djangostudentform'),
    path('password_validation/', views.PasswordValidation,
         name='passwordvalidation'),
]
