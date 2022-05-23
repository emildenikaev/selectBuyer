from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import ADMINS
from app import BotDB

from loader import dp, bot
from states.states import Mailing


@dp.message_handler(user_id=ADMINS, commands=["tell_everyone"])
async def mailing(message: types.Message):
    await message.answer(("Пришлите текст рассылки"))
    await Mailing.Text.set()


@dp.message_handler(user_id=ADMINS, state=Mailing.Text)
async def mailing(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text="Отправить", callback_data="text_send")],
        ]
    )
    await message.answer((f"Нажмите, чтобы отправить текст\n\n"
                           f"{text}").format(text=text),
                         reply_markup=markup)
    await Mailing.Send.set()


@dp.callback_query_handler(user_id=ADMINS, state=Mailing.Send)
async def mailing_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    await state.reset_state()
    await call.message.edit_reply_markup()

    users = BotDB.get_all_users()
    for user in users:
        try:
            await bot.send_message(user[0],
                                   text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer(("Рассылка выполнена."))


