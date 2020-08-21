from rest_framework import serializers

from .models import Hospital


class HospitalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name', 'contact_address', 'contact_number']
