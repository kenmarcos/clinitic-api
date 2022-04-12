from django.urls import path
from .views import DoctorCreateView


urlpatterns = [
    path('doctors/', DoctorCreateView.as_view())
]
