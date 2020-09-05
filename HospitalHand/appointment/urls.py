from django.urls import path
from . import views

app_name = 'appointment'

# Url till this app: /appointment/

urlpatterns = [
    path('create/', views.CreateAppointment.as_view(), name='createappointment'),
    path('hospital/update/<int:id>', views.FixAppointmentUpdate.as_view(), name='fixappointmentupdate'),
    path('hospital/<str:authentication_token>', views.FixAppointmentList.as_view(), name='fixappointmentlist'),

    path('profile/<str:authentication_token>', views.ProfileAppointment.as_view(), name='profileappointment'),
    path('profile/update/<int:id>', views.UpdateAppointment.as_view(), name='updateappointment'),
    path('profile/delete/<int:id>', views.DeleteAppointment.as_view(), name='deleteappointment'),

]
