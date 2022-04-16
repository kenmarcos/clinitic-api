from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        exclude = ['doctor']
        depth= 1

class AppointmentCancelSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Appointment
        fields = '__all__'
        read_only_fields = ['title', 'start', 'end', 'doctor', 'patient']
        extra_kwargs = {'isActive': {'required': True}}