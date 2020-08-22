from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .serializers import DoctorsModelSerializer, DepartmentModelSerializer
from .models import Doctor, Department


# Using generic Views

class DoctorsModelCreateAPIView(CreateAPIView):
    serializer_class = DoctorsModelSerializer


class DoctorsModelUpdateAPIView(UpdateAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()


class DoctorsModelDestroyAPIView(DestroyAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()


class DoctorsModelListAPIView(ListAPIView):
    serializer_class = DoctorsModelSerializer
    lookup_field = "department"

    def get_queryset(self):
        department = self.kwargs['department']
        return Doctor.objects.filter(department=department)


class DepartmentModelListAPIView(ListAPIView):
    serializer_class = DepartmentModelSerializer
    queryset = Department.objects.all()
