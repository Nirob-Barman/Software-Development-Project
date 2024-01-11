from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppointmentSerializer
from .models import Appointment

# Create your views here.

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # custom query
    def get_queryset(self):
        # return self.queryset
        querySet = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')

        if patient_id:
            querySet = querySet.filter(patient_id=patient_id)
        return querySet