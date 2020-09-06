from django.db import models

from hospital.models import Hospital
from userauth.models import CustomUser
from categories.models import Doctor


# Create your models here.

class Appointment(models.Model):
    # authentication_token = models.CharField(max_length=200)
    patient_name = models.CharField(max_length=200)
    patient_problem_description = models.TextField(max_length=500)
    medicines_taken = models.TextField(max_length=200, null=True)
    doctor_requested = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fixed_appointment = models.BooleanField(default=False)
    appointment_date = models.DateField(default=None, null=True,blank=True)
    appointment_time = models.TimeField(default=None, null=True,blank=True)
    date_posted = models.DateField(auto_now=True)
    select_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name
