import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from bot.models import User
from djangobot.config import SECRET


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print('start authenticate')
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            print('cant to read header')
            return None
        try:
            token = authorization_header.split()[1]
            print('token',token)
            print(SECRET)
            payload = jwt.decode(token, SECRET, algorithms=['HS256'])
            print("payload",payload)
            user = User.objects.get(login=payload['login'])
            print(user)
            print('SUCCESS!')
            return (user, None)
        except jwt.ExpiredSignatureError:
            print('expired')
            raise AuthenticationFailed('Token has expired')
        except (jwt.DecodeError, User.DoesNotExist):
            print('fail decoder')
            pass
        return None

