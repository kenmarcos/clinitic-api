from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)

        user = self.model(email=email,
	                      is_staff=is_staff, is_active=True,
	                      is_superuser=is_superuser, last_login=now,
	                      date_joined=now, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Doctor(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    email = models.EmailField(max_length=255, unique=True)
    crm_number = models.CharField(max_length=6, unique=True)
    username = models.CharField(unique=False, null=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'crm_number']

    objects = CustomUserManager()