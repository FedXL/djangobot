from django.contrib import admin
from django.urls import path


from bot.views import UsersHandler, AccessTokenObtainView, JwtObrainView, HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/',HelloWorld.as_view(),name='hello'),
    path('api/user/', UsersHandler.as_view(), name='user handler create/delete/update point'),
    path('api/auth2/',JwtObrainView.as_view(),name='standart')

]
