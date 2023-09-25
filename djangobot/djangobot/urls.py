from django.contrib import admin
from django.urls import path


from bot.views import UsersHandler, JwtObrainView, CabinetUserView, MessagesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UsersHandler.as_view(), name='user handler create/delete/update point'),
    path('api/auth/',JwtObrainView.as_view(),name='authorization point'),
    path('api/cabinet/', CabinetUserView.as_view(), name='get token for the telegram bot'),
    path('api/send_message/', MessagesView.as_view(), name="send/get messages bot_token required")
]
