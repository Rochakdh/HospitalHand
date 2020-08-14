from django.urls import path
from .views import DoctorsModelCreateAPIView, DoctorsModelListAPIView

urlpatterns = [
    path('create/', DoctorsModelCreateAPIView.as_view()),
    path('list/', DoctorsModelListAPIView.as_view()),

]
