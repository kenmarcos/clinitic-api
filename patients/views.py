from rest_framework.generics import ListCreateAPIView
from .serializers import PatientSerializer
from .models import Patient


class PatientListCreateView(ListCreateAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
