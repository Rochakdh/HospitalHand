from django.urls import path
from .views import DoctorsModelCreateAPIView, DoctorsModelListAPIView

urlpatterns = [
    path('create/', DoctorsModelCreateAPIView.as_view()),
    path('list/<int:department>/', DoctorsModelListAPIView.as_view()),

]
