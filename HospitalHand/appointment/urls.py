from django.urls import path
from . import views
app_name = 'appointment'


# Url till this app: /appointment/

urlpatterns = [
    path('<int:id>/', views.CreateAppointment.as_view() , name ='createappointment'),
    path('hospital/<int:pk>', views.FixAppointment.as_view() , name ='fixappointment'),
]