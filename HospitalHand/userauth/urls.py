from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'userauth'

# Url till this app: /user/

urlpatterns = [

    path('login/', obtain_auth_token, name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('update/<uuid:id>/', views.UpdateUserView.as_view(), name='update'),

]
