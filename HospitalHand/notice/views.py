from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework.generics import CreateAPIView,ListAPIView

from .forms import notice_form
from .models import notice_model
from .serializers import notice_serializers
from .task import sleepy



class notice_view(CreateAPIView):
    serializer_class=notice_serializers

class notice_list_view(ListAPIView):
    sleepy(10)
    serializer_class=notice_serializers
    queryset=notice_model.objects.all()

    