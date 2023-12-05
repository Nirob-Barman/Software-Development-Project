from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('django_form/', views.DjangoForm, name='djangoForm'),
]
