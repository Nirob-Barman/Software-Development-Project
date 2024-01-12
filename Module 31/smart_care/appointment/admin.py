from django.contrib import admin
from .models import Appointment

# for sending email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
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

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject = "Your appointment is Running"
            email_body = render_to_string(
                'appointment/email_templates/admin_mail.html', {'user': obj.patient.user, 'doctor': obj.doctor}
            )
            email = EmailMultiAlternatives(subject=email_subject, body=email_body, to=[obj.patient.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
admin.site.register(Appointment, AppointmentModelAdmin)