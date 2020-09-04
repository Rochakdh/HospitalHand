from rest_framework import serializers
from appointment.models import Appointment
from categories.models import Doctor
from hospital.models import Hospital


class AppointmentSerializers(serializers.ModelSerializer):
    doctor_requested = serializers.SlugRelatedField(queryset=Doctor.objects.all(), slug_field='name', many=False)
    select_hospital = serializers.SlugRelatedField(queryset=Hospital.objects.all(), slug_field='hospital_name',
                                                   many=False)

    class Meta:
        model = Appointment
        fields = ['id', 'authentication_token', 'fixed_appointment', 'doctor_requested', 'patient_name',
                  'patient_problem_description',
                  'medicines_taken', 'appointment_time', 'appointment_date', 'select_hospital']
        # read_only_fields = ['fixed_appointment', 'appointment_time']

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=("patient_name", "appointment_date", "appointment_time"),
                message="The Appointment is already fixed for You. Thank You !"
            )
        ]


class AppointmentFixSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['fixed_appointment','patient_name', 'appointment_time', 'appointment_date', 'select_hospital',
                  'doctor_requested']


class AppointmentUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointment_time', 'appointment_date', 'patient_name']
