from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from . import serializers
# Create your views here.

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer

