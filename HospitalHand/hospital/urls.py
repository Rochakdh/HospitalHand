from django.urls import path
from .views import DoctorsModelListAPIView, DoctorsModelCreateAPIView

urlpatterns = [
    path('list/', DoctorsModelListAPIView.as_view()),
    path('create/', DoctorsModelCreateAPIView.as_view())

]
