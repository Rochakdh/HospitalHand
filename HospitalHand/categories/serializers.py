from rest_framework import serializers

from .models import Doctor


class DoctorsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'added_on', 'department', 'id']
        read_only_fields = ['id']
