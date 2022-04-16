from django.urls import path
from .views import AppointmentCreateView, AppointmentListView, AppointmentListByDoctorView, AppointmentCancelView


urlpatterns = [
    path('appointments/patients/<str:patient_id>/', AppointmentCreateView.as_view()),
    path('appointments/', AppointmentListView.as_view()),
    path('appointments/doctors/<str:doctor_id>/', AppointmentListByDoctorView.as_view()),
    path('appointments/<str:appointment_id>/', AppointmentCancelView.as_view())
]
