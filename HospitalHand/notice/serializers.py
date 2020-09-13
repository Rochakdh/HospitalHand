from rest_framework import serializers

from hospital.models import Hospital
from .models import notice_model


class notice_serializers(serializers.ModelSerializer):
    class Meta:
        model = notice_model
        fields = ['id', 'title', 'description', 'post_at']
