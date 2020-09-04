from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import AppointmentSerializers, AppointmentFixSerializers, AppointmentUpdateSerializers
from .models import Appointment


# Create your views here.

class CreateAppointment(ListCreateAPIView):
    serializer_class = AppointmentSerializers
    queryset = Appointment.objects.all()
    # lookup_field = 'id'


class FixAppointmentUpdate(UpdateAPIView):
    serializer_class = AppointmentFixSerializers
    queryset = Appointment.objects.all()


class FixAppointmentList(ListAPIView):
    serializer_class = AppointmentFixSerializers
    queryset = Appointment.objects.all()


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
