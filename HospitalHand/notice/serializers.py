from rest_framework import serializers
from .models import notice_model

class notice_serializers(serializers.ModelSerializer):
    class Meta:
        model=notice_model
        fields=['id','title','description','post_at']