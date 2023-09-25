import random
import string
from datetime import datetime,timedelta
import jwt
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from bot.models import User, Token, TeleUser, Message
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

def get_user_by_bot_token(token: str) -> tuple[User, TeleUser] | tuple[None, None]:
    try:
        token_obj = Token.objects.get(token=token)
        user = token_obj.user
        tele_user: TeleUser = TeleUser.objects.get(user=user)
        return user,tele_user
    except:
        return None, None

def send_message_to_bot(name, user_id, text):
    message_text = (
        f"{name} я получил от тебя сообщение.\n"
        f"{text}"
    )
    bot.send_message(user_id,message_text,parse_mode='HTML')

def create_bot_token(user) -> str | bool:
    token = generate_random_token(length=25)
    try:
        register_token = Token(user=user, token=token)
        register_token.save()
    except IntegrityError:
        token_obj = Token.objects.get(user=user)
        token_obj.token =token
        token_obj.save()
    except Exception as er:
        print(er)
        return False
    return token


def generate_random_token(length=25):
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choice(characters) for _ in range(length))
    return token


def save_message(message_type, message_text, user):
    try:
        message = Message(user=user,
                          type=message_type,
                          text=message_text)
        message.save()
        return True
    except:
        return False

def check_code(user: User, code):
    try:
        tele_user: TeleUser = TeleUser.objects.get(pk=int(code))
        tele_user.user = user
        tele_user.save()
        print('ТелеЮзер удачно связан с юзером')
        return True
    except TeleUser.DoesNotExist:
        print('Телепузик не найден')
        return False
    except Exception as ER:
        print(ER)
        return False

