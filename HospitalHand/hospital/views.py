from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import HospitalModelSerializer
from .models import Hospital


# Using generic Views

class DoctorsModelCreateAPIView(CreateAPIView):
    serializer_class = HospitalModelSerializer


class DoctorsModelListAPIView(ListAPIView):
    serializer_class = HospitalModelSerializer
    queryset = Hospital.objects.all()
