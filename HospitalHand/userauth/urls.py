from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

from .views import UserViewSet, CustomAuthToken

app_name = 'userauth'

router = DefaultRouter()
router.register('', UserViewSet, basename='user_view')

# Url till this app: /user/

urlpatterns = [

                  path('login/', CustomAuthToken.as_view(), name='login'),
                  path('signup/', views.SignUpView.as_view(), name='signup'),
                  # path('update/<uuid:id>/', views.UpdateUserView.as_view(), name = 'update' ),
                  # path('profile/<str:username>',views.GetUserAPIView.as_view(),name='profile')

              ] + router.urls

# standard
# django
# 3rd party library
# external local
# internal local
