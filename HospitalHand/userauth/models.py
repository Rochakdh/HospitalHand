from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Contacts ( models.Model ):
    """
    Contacts is Abstract Base Class and is used in Models CustomUser,
    """
    contact_address = models.CharField ( max_length = 150 )
    contact_number  = models.IntegerField ()

    class Meta:
        abstract = True

class CustomUser ( AbstractUser , Contacts):
    """
    Custom User Model to add additional attributes to User Model
    """
    middle_name = models.CharField ( max_length = 120 )
    date_of_birth = models.DateTimeField ()
    profile_pictures = models.ImageField ( blank=True )
    REQUIRED_FIELDS = ['date_of_birth', 'contact_number']





