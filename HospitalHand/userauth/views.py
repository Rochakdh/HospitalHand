from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.response import Response

from . serializers import CustomUserModelSearializers
from django.contrib.auth import get_user_model
from .models import CustomUser

USER = get_user_model()
class SignUpView(CreateAPIView):
    """
    Sign Up functionality for creating object of
    Custom User Model with CustomUserModelSearializers
    """
    serializer_class = CustomUserModelSearializers

class UpdateUserView(UpdateAPIView):
    """
        Updating User Profile of CustomUser
    """
    serializer_class = CustomUserModelSearializers
    lookup_field = 'id'
    queryset = CustomUser.objects.all()










