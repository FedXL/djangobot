import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from bot.models import User
from djangobot.config import SECRET


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        try:
            token = authorization_header.split()[1]
            payload = jwt.decode(token, SECRET, algorithms=['HS256'])
            user = User.objects.get(login=payload['login'])
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except (jwt.DecodeError, User.DoesNotExist):
            print('[fail decoder]')
            pass
        return None

