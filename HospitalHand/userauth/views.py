from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken


from . serializers import CustomUserModelSerializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from .permissions import CustomIsAuthenticated
USER = get_user_model()
class SignUpView(CreateAPIView):
    """
    Sign Up functionality for creating object of
    Custom User Model with CustomUserModelSearializers
    """
    serializer_class = CustomUserModelSerializers


# class GetUserAPIView(RetrieveAPIView):
#     serializer_class = CustomUserModelSearializers
#     queryset = CustomUser.objects.all()
#     lookup_field = 'username'
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [CustomIsAuthenticated]
#
# class UpdateUserView(UpdateAPIView):
#     """
#         Updating User Profile of CustomUser
#     """
#     serializer_class = CustomUserModelSearializers
#     lookup_field = 'id'
#     queryset = CustomUser.objects.all()

class UserViewSet(ModelViewSet):
    http_method_names = ['get','put','patch','delete']
    serializer_class = CustomUserModelSerializers
    queryset = CustomUser.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomIsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        super(UserViewSet, self).get_queryset()
        print(self.request.user.id)
        return self.queryset.filter(id=self.request.user.id)






class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,'id':token.user.id})
