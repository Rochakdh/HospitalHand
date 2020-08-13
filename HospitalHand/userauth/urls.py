from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'userauth'

urlpatterns = [

    path( 'login/' , obtain_auth_token, name = 'login' ),

]