from django.urls import path
from .views import DoctorsModelCreateAPIView, DoctorsModelListAPIView, DepartmentModelListAPIView, \
    DoctorsModelDestroyAPIView, DoctorsModelUpdateAPIView

urlpatterns = [
    path('create/', DoctorsModelCreateAPIView.as_view()),
    path('list/<int:department>/', DoctorsModelListAPIView.as_view()),

    path('delete/<int:pk>/', DoctorsModelDestroyAPIView.as_view()),
    path('update/<int:pk>/', DoctorsModelUpdateAPIView.as_view()),

    path('alldepartment/', DepartmentModelListAPIView.as_view())

]
