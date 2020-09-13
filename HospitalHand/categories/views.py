from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,RetrieveAPIView
from .serializers import DoctorsModelSerializer, DepartmentModelSerializer,DoctorsModelListSerializer
from .models import Doctor, Department
from .permissions import HospitalIsAuthenticated,HospitalIsObjectAuthenticated
from hospital.models import Hospital

# Using generic Views

class DoctorsModelCreateAPIView(CreateAPIView):
    serializer_class = DoctorsModelSerializer
    permission_classes = [HospitalIsAuthenticated]




class DoctorsModelUpdateAPIView(UpdateAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()

class DoctorsModelDestroyAPIView(DestroyAPIView):
    serializer_class = DoctorsModelSerializer
    queryset = Doctor.objects.all()

class DoctorsModelListAPIView(ListAPIView):
    serializer_class = DoctorsModelListSerializer
    queryset = Doctor.objects.all()
    permission_classes = [HospitalIsObjectAuthenticated,HospitalIsAuthenticated]
    # #
    def get_queryset(self):
        super(DoctorsModelListAPIView, self).get_queryset()
        get_hospital_id = Hospital.objects.get(name=self.request.user.id)
        print(self.request.user.id)
        return self.queryset.filter(hospital=get_hospital_id)

class DepartmentModelListAPIView(ListAPIView):
    serializer_class = DepartmentModelSerializer
    queryset = Department.objects.all()






