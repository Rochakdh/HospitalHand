from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,UpdateAPIView
from .serializers import AppointmentSerializers,AppointmentFixSerializers
from .models import Appointment
# Create your views here.

class CreateAppointment(ListCreateAPIView):
    serializer_class = AppointmentSerializers
    queryset = Appointment.objects.all()
    # lookup_field = 'id'

class FixAppointment(UpdateAPIView):
    serializer_class = AppointmentFixSerializers
    queryset = Appointment.objects.all()



