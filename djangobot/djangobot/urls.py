from django.contrib import admin
from django.urls import path


from bot.views import UsersHandler, JwtObrainView, HelloWorld, CabinetUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/',HelloWorld.as_view(),name='hello'),
    path('api/user/', UsersHandler.as_view(), name='user handler create/delete/update point'),
    path('api/auth/',JwtObrainView.as_view(),name='authorization point'),
    path('api/get_token/', CabinetUserView.as_view(), name='get token for the telegram bot')
]
