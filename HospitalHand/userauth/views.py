from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from . serializers import CustomUserModelSearializers
from django.contrib.auth import get_user_model
from .models import CustomUser

USER = get_user_model()
class SignUpView(CreateAPIView):
    """
    Sign up functionality for creating object of Custom User Model with CustomUserModelSearializers
    """
    serializer_class = CustomUserModelSearializers



