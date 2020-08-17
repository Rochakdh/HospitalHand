from django.contrib import admin
from .models import Doctor, Department

# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
