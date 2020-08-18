from django.db import models

from django.utils import timezone


class Department(models.Model):
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name


class Doctor(models.Model):
    name = models.CharField(unique=True, max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.name
