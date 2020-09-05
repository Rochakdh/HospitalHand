from django.urls import path
from .views import HospitalModelListAPIView

urlpatterns = [
    path('list/', HospitalModelListAPIView.as_view()),

]