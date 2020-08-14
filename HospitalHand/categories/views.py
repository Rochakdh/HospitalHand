from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import DoctorsModelSerializer
from .models import Doctor


# Using generic Views

class DoctorsModelCreateAPIView(CreateAPIView):
    serializer_class = DoctorsModelSerializer


class DoctorsModelListAPIView(ListAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()
