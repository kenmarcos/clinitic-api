from django.db import models
import uuid


class Patient(models.Model):

    SEX_OPTIONS = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS)
    birth_date = models.DateField()
