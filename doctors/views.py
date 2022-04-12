from rest_framework.generics import CreateAPIView
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorCreateView(CreateAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
