from django.urls import path
from .views import HospitalModelListAPIView, HospitalModelCreateAPIView, HospitalModelDestroyAPIView, \
    HospitalModelUpdateAPIView

urlpatterns = [
    path('list/', HospitalModelListAPIView.as_view()),
    path('create/', HospitalModelCreateAPIView.as_view()),
    path('update/<int:pk>', HospitalModelUpdateAPIView.as_view()),
    path('delete/<int:pk>', HospitalModelDestroyAPIView.as_view()),

]
