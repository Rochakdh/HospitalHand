import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Contacts(models.Model):
    """
    Contacts is Abstract Base Class and is used in Models CustomUser,
    """

    contact_address = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=10, blank=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, Contacts):
    """
    Custom User Model to add additional attributes to User Model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    middle_name = models.CharField(max_length=120, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_pictures = models.ImageField(blank=True, null=True)
    is_hospital = models.BooleanField(default=False)
    # REQUIRED_FIELDS = ['date_of_birth', 'contact_number']

