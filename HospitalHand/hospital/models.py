from django.db import models
from userauth.models import Contacts

'''
Model For Hospitals and their relation with Doctors
'''


class Hospital(Contacts):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.name)


