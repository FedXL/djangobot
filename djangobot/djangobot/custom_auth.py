from django.contrib.auth.backends import ModelBackend
from bot.models import User


class CustomDatabaseAuth(ModelBackend):
    def authenticate(self, request, login=None, psw=None, **kwargs):
        try:
            user = User.objects.get(login=login)  # Здесь укажите поле, по которому будете искать пользователя
            if user.check_password(psw):
                return user
        except User.DoesNotExist:
            return None