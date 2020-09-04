from django.urls import path
from .views import DoctorsModelListAPIView

urlpatterns = [
    path('list/', DoctorsModelListAPIView.as_view()),

]