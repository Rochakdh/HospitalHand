from django.db import models
from userauth.models import CustomUser
# Create your models here.

class Appointment(models.Model):
    patient_name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    patient_problem_description = models.TextField(max_length=500)
    upload_prescription_photo = models.ImageField( blank=True )
    medicines_taken = models.TextField(max_length=200)






