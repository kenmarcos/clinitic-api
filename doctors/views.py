from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView, Response, status
from .models import Doctor
from .serializers import DoctorSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class DoctorCreateView(CreateAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        doctor = authenticate(**serializer.validated_data)

        if doctor:
            token = Token.objects.get_or_create(user=doctor)[0]
            return Response({'token': token.key})
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class DoctorRetrieveView(RetrieveAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    lookup_url_kwarg = 'email'
    lookup_field = 'email'
