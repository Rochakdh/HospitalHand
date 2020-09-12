import uuid
from django.db import models
from userauth.models import Contacts, CustomUser

'''
Model For Hospitals and their relation with Doctors
'''


class Hospital(Contacts):
    name = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.hospital_name)
