import os
import django
import telebot

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangobot.settings")
django.setup()

from bot.models import TeleUser
from djangobot.config import BOT_TOKEN

API_TOKEN = BOT_TOKEN
bot = telebot.TeleBot(API_TOKEN, skip_pending=True)



def send_message_to_bot(name, user_id, text):
    message_text = (
        f"{name} я получил от тебя сообщение.\n"
        f"{text}"
    )
    bot.send_message(user_id,message_text,parse_mode='HTML')





@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_data = {
        'first_name': message.from_user.first_name,
        'second_name': message.from_user.last_name,
        'user_name': message.from_user.username,
        'telegram_user_id': message.from_user.id,
    }

    if TeleUser.objects.filter(telegram_user_id=message.from_user.id).exists():
        code = TeleUser.objects.get(telegram_user_id=message.from_user.id).pk
    else:
        TeleUser.objects.create(**user_data)
        code = user_data['pk']

    if len(str(code)) < 4:
        str_code = str(code)
        while True:
            str_code = '0' + str_code
            if len(str_code) == 4:
                break
    else:
        str_code = str(code)

    message_text = (
        f"Добро пожаловать 👋👋👋\n"
        f"Ваш номер для регистрации в системе: <code>{str_code}</code>\n"
        f"Введите код в нашем сервисе для получения токена."
    )

    bot.reply_to(message, message_text, parse_mode='HTML')



def main():
    bot.infinity_polling()
