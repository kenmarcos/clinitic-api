from rest_framework.generics import CreateAPIView, ListAPIView
from appointments.serializers import AppointmentSerializer
from .models import Appointment
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AppointmentCreateView(CreateAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer = serializer.save(doctor=self.request.user, patient_id=self.kwargs['patient_id'])

        return super().perform_create(serializer)


class AppointmentListView(ListAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


    def filter_queryset(self, queryset):

        if 'date' in self.request.query_params:
            date = self.request.GET.get('date')
            queryset = queryset.filter(start__icontains=date)

        return super().filter_queryset(queryset)


class AppointmentListByDoctorView(ListAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    lookup_url_kwarg = 'doctor_id'

    def filter_queryset(self, queryset):
        doctor_id = self.kwargs['doctor_id']
        queryset = queryset.filter(doctor_id=doctor_id)

        return super().filter_queryset(queryset)
