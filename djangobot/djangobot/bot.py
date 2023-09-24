from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor



import aiogram.utils.markdown as md

from djangobot.bot.models import TeleUser
from djangobot.djangobot.config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot )

@dp.message_handler(commands=['start'], state="*")
async def welcome_message(message: types.Message):
    if TeleUser.objects.filter(telegram_user_id=message.from_user.id).exists():
        user = TeleUser.objects.filter(telegram_user_id=message.from_user.id)
        code = user.pk
    else:

        user = TeleUser(first_name=message.from_user.first_name,
                            second_name=message.from_user.last_name,
                            user_name=message.from_user.username,
                            telegram_user_id=message.from_user.id)

        user.save()
        code = user.pk

    text = md.text(
        md.text("Добро пожаловать 👋👋👋"),
        md.text("Ваш номер для регистрации в сиcтеме: ",f"<code>+{code}+</code>"),
        md.text("Введите код в нашем сервисе для получения токена.")
    )

    await bot.send_message(message.from_user.id,text,parse_mode=ParseMode.HTML)
    await bot.send_message(message.from_user.id, "хаюшки",
                           parse_mode=ParseMode.HTML)



def main():
    executor.start_polling(dp,
                           skip_updates=True)
if __name__ == "__main__":
    main()