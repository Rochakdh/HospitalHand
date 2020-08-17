from django.db import models
from userauth.models import CustomUser
from categories.models import Doctor
# Create your models here.

class Appointment(models.Model):
    patient_name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    patient_problem_description = models.TextField(max_length=500)
    upload_prescription_photo = models.ImageField( blank=True,null=True)
    medicines_taken = models.TextField(max_length=200,null=True)
    doctor_requested = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    fixed_appointment = models.BooleanField(default=False)
    appointment_time = models.DateTimeField(default=None,blank=True,null=True)
    date_posted = models.DateField(auto_now=True)

    def year(self):
        return self.date_posted.year
    def month(self):
        return self.date_posted.month
    def day (self):
        return self.date_posted.day

