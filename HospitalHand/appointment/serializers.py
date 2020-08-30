from rest_framework import serializers
from appointment.models import Appointment

class AppointmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['url','doctor_requested']
        read_only_fields = ['fixed_appointment','appointment_time']



class AppointmentFixSerializers(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['fixed_appointment','appointment_time']


