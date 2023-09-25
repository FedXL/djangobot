from datetime import datetime,timedelta
from typing import Tuple

import jwt
from django.contrib.auth.hashers import check_password

from bot.models import User, Token, TeleUser
from djangobot.config import SECRET

from telegram_bot.bot import bot


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

def get_user_by_bot_token(token) -> Tuple[User,TeleUser] | None:
    try:
        token_obj: Token = Token.objects.get(token=token)
        user = token_obj.user
        tele_user: TeleUser = TeleUser.objects.get(user=user)
        return user,tele_user
    except :
        return None

def send_message_to_bot(name, user_id, text):
    message_text = (
        f"{name} я получил от тебя сообщение.\n"
        f"{text}"
    )
    bot.send_message(user_id,message_text,parse_mode='HTML')
