from django.contrib import admin
from django.urls import path

from bot.views import UserMessagesView, HelloWorld, UsersHandler
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', HelloWorld.as_view(), name='hello-world'),
    path('api/user/', UsersHandler.as_view(), name='user handler create/delete/update point'),
    # path('api/autorisation/',Autorisation.as_view(),name='get access token')

]
