from django.contrib import admin
from .models import Appointment
# Register your models here.

class AppointmentModelAdmin(admin.ModelAdmin):
    # list_display = ('patient', 'doctor', 'appointment_types','appointment_status', 'symptoms', 'date', 'cancel')
    list_display = ('patient_name', 'doctor_name', 'appointment_types','appointment_status', 'symptoms', 'date', 'cancel')
    
    def doctor_name(self, obj):
        # return obj.doctor.user.get_full_name() if obj.doctor.user else "N/A"
        return obj.doctor.user.first_name + ' ' + obj.doctor.user.last_name
    
    def patient_name(self, obj):
        # return obj.patient.user.get_full_name() if obj.patient.user else "N/A"
        return obj.patient.user.first_name + ' ' + obj.patient.user.last_name

    # def patient_name(self, obj):
    #     return obj.user.first_name + ' ' + obj.user.last_name

    # def doctor_name(self, obj):
    #     return obj.user.first_name + ' ' + obj.user.last_name

admin.site.register(Appointment, AppointmentModelAdmin)