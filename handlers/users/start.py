from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.choice_buttons import start_info
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Это чат-бот, где ты можешь подробнее узнать о заказе телеграмм-бота или сайта")
    await bot.send_photo(chat_id=message.chat.id, photo=open("photos/robot_photo.png", "rb"))

    await message.answer(text="Расскажу подробнее?",
                         reply_markup=start_info)
