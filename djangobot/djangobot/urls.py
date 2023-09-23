from django.contrib import admin
from django.urls import path

from bot.views import UserMessagesView, HelloWorld, UsersHandler

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/user_messages/', UserMessagesView.as_view(), name='user-messages'),
    path('api/hello/', HelloWorld.as_view(), name='hello-world'),
    path('api/user/', UsersHandler.as_view(), name='user handler point')
]
