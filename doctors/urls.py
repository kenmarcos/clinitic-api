from django.urls import path
from .views import DoctorCreateView, LoginView


urlpatterns = [
    path('doctors/', DoctorCreateView.as_view()),
    path('login/', LoginView.as_view())
]
