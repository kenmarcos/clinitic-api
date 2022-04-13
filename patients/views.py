from rest_framework.generics import ListAPIView
from .serializers import PatientSerializer
from .models import Patient


class PatientListView(ListAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
