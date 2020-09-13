from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from hospital.models import Hospital
from userauth.models import CustomUser
from .serializers import AppointmentSerializers, AppointmentFixSerializers, AppointmentUpdateSerializers
from .models import Appointment
from .permissions import HospitalIsAuthenticated


# Create your views here.

class CreateAppointment(ListCreateAPIView):
    serializer_class = AppointmentSerializers
    queryset = Appointment.objects.all()


class FixAppointmentUpdate(UpdateAPIView):
    serializer_class = AppointmentFixSerializers
    queryset = Appointment.objects.all()
    lookup_field = 'id'


class FixAppointmentList(ListAPIView):
    serializer_class = AppointmentFixSerializers
    queryset = Appointment.objects.all()

    def get_queryset(self):
        super(FixAppointmentList, self).get_queryset()
        get_hospital_id = Hospital.objects.get(name=self.request.user.id)
        print(self.request.user.id)
        return self.queryset.filter(select_hospital=get_hospital_id)


class ProfileAppointment(ListAPIView):
    serializer_class = AppointmentSerializers
    queryset = Appointment.objects.all()
    lookup_field = "authentication_token"

    def get_queryset(self):
        authentication_token = self.kwargs['authentication_token']
        return Appointment.objects.filter(authentication_token=authentication_token)


class UpdateAppointment(RetrieveUpdateAPIView):
    serializer_class = AppointmentUpdateSerializers
    queryset = Appointment.objects.all()
    lookup_field = 'id'


class DeleteAppointment(DestroyAPIView):
    serializer_class = AppointmentSerializers
    queryset = Appointment.objects.all()
    lookup_field = 'id'
