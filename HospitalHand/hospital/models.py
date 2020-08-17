from django.db import models
from userauth.models import Contacts
from categories.models import Doctor
# Create your models here.

class Hospital(Contacts):
    name = models.CharField(max_length=150)
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.name


