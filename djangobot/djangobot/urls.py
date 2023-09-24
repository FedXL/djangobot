from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from bot.views import UsersHandler, AccessTokenObtainView, CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UsersHandler.as_view(), name='user handler create/delete/update point'),
    path('api/auth/', AccessTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/auth2/',CustomTokenObtainPairView.as_view(),name='standart')

]
