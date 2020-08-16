from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework.generics import CreateAPIView,ListAPIView

from .forms import notice_form
from .models import notice_model
from .serializers import notice_serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes

class notice_view(CreateAPIView):
    serializer_class=notice_serializers

class notice_list_view(ListAPIView):
    serializer_class=notice_serializers
    qs=notice_model.objects.all()

    def get_queryset(self):
        return notice_model.objects.all()