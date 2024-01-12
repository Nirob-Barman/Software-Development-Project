from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from .models import Doctor, Specialization, Designation, AvailableTime, Review
from .serializers import DoctorSerializer, SpecializationSerializer, DesignationSerializer, AvailableTimeSerializer, ReviewSerializer

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1  # Number of items per page
    page_size_query_param = 'page_size'  # Query parameter for page size
    max_page_size = 10  # Maximum number of items per page


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name']
    pagination_class = DoctorPagination


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class AvailableTimeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
