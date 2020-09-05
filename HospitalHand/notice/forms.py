from django.forms import ModelForm
from datetime import datetime,date
from .models import notice_model

class notice_form(ModelForm):
    class Meta:
        model=notice_model
        fields=['title','description','post_at']
