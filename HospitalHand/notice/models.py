from django.db import models

from hospital.models import Hospital


class notice_model(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    post_at = models.DateField()

    def __str__(self):
        return self.title
