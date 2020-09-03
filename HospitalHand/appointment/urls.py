from django.urls import path
from . import views

app_name = 'appointment'

# Url till this app: /appointment/

urlpatterns = [
    path('create/', views.CreateAppointment.as_view(), name='createappointment'),
    path('hospital/<int:pk>', views.FixAppointment.as_view(), name='fixappointment'),
    path('profile/<str:authentication_token>', views.ProfileAppointment.as_view(), name='profileappointment'),
    path('profile/update/<int:id>', views.UpdateAppointment.as_view(), name='updateappointment'),
    path('profile/delete/<int:id>', views.DeleteAppointment.as_view(), name='deleteappointment'),

]
