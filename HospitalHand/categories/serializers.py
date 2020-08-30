from rest_framework import serializers

from .models import Doctor, Department

from hospital.models import Hospital


class DoctorsModelSerializer(serializers.ModelSerializer):
    hospital = serializers.SlugRelatedField(queryset=Hospital.objects.all(), slug_field='name', many=True)

    class Meta:
        model = Doctor
        fields = ['name', 'experience', 'department', 'hospital', 'id']
        read_only_fields = ['id']


class DepartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name', 'id']
        read_only_fields = ['id']
