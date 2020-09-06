from django.urls import path
from .views import notice_view, notice_list_view, notice_delete_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('notice/', notice_view.as_view()),
    path('notice/update_delete/<int:pk>/', notice_delete_view.as_view()),
    path('notice/list/', notice_list_view.as_view()),
    path('auth/', obtain_auth_token),
]
