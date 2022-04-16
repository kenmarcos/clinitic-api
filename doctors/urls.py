from django.urls import path
from .views import DoctorCreateView, LoginView, DoctorRetrieveView


urlpatterns = [
    path('doctors/', DoctorCreateView.as_view()),
    path('login/', LoginView.as_view()),
    path('doctors/<str:email>/', DoctorRetrieveView.as_view())
]
