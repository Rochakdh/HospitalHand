from rest_framework import serializers

from .models import Doctor


class DoctorsModelSerializer(serializers.ModelSerializer):
    hospital = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)

    class Meta:
        model = Doctor
        fields = ['name', 'experience', 'department', 'hospital', 'id']
        read_only_fields = ['id']
