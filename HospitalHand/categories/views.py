from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,RetrieveAPIView
from .serializers import DoctorsModelSerializer, DepartmentModelSerializer
from .models import Doctor, Department
from .permissions import HospitalIsAuthenticated


# Using generic Views

class DoctorsModelCreateAPIView(CreateAPIView):
    serializer_class = DoctorsModelSerializer
    permission_classes = [HospitalIsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'




class DoctorsModelUpdateAPIView(UpdateAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()

class DoctorsModelDestroyAPIView(DestroyAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()

class DoctorsModelListAPIView(ListAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()
    lookup_field = "department"

    def get_queryset(self):
        department = self.kwargs['department']
        return Doctor.objects.filter(department=department)

class DepartmentModelListAPIView(ListAPIView):
    serializer_class = DepartmentModelSerializer
    queryset = Department.objects.all()






