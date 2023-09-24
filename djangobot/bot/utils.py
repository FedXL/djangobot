from datetime import datetime,timedelta

import jwt
from django.contrib.auth.hashers import check_password

from bot.models import User
from djangobot.config import SECRET


def create_token(login):
    payload = {
        'login': login,
        'exp': int((datetime.utcnow() + timedelta(days=1)).timestamp()),  # Преобразуйте в timestamp
        'iat': int(datetime.utcnow().timestamp()),  # Преобразуйте в timestamp
    }
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return token

def is_authenticate(login,psw):
    try:
        user = User.objects.get(login=login)
    except:
        return False

    if check_password(psw,user.psw):
        return True
    else:
        return False

