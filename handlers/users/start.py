from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from app import BotDB


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if (not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
    await bot.send_photo(chat_id=message.chat.id, photo=open("photos/robot_photo.png", "rb"), caption=(
        f"Привет, {message.from_user.full_name}🤖 \n\n"
        f"Это тестовый бот технической поддержки, где Вы сможете задать интересующий вопрос по ботам, а заодно и посмотреть принцип "
        f"работы такого бота в действии🌚\n\n"
        f"Еще бот умеет осуществлять рассылку всем пользователям с полезной информации по развитию своего проекта, "
        f"будь то телеграм боты или сайты📊\n\n"
        f"Если хотите задать конкретный вопрос, введите команду /support \n"
        f"Если хотите пообщаться с оператором, введите команду /support_call"))
