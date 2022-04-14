from django.db import models
import uuid


class Appointment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField(null=True)
    isActive = models.BooleanField(default=True)

    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='appointments')
