from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'email', 'crm_number', 'password']

        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
