from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

# Create your models here.

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    # ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
    ('Missed', 'Missed'),
    ('Rescheduled', 'Rescheduled'),
    # ('Postponed', 'Postponed'),
    # ('No Show', 'No Show'),
]
APPOINTMENT_TYPES = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    ('Face-to-Face', 'Face-to-Face'),
    ('Physical', 'Physical'),
    ('Teleconsultation', 'Teleconsultation'),
    ('Virtual', 'Virtual'),
    ('In-Person', 'In-Person'),
    ('Out-Person', 'Out-Person'),
    ('Other', 'Other'),
]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(
        max_length=50, choices=APPOINTMENT_TYPES)
    appointment_status = models.CharField(
        max_length=50, choices=APPOINTMENT_STATUS, default='Pending')
    symptoms = models.TextField()
    # time = models.OneToOneField(AvailableTime, on_delete=models.CASCADE)
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return f"Patient: {self.patient} - Doctor: {self.doctor} - {self.appointment_types}"
