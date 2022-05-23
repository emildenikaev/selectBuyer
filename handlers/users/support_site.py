from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import cost
from loader import dp


@dp.callback_query_handler(info_callback.filter(item_name="supportsite"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"⚡️Бот для оптимизации продаж \n"
        f"⚡️Для рассылки сообщений \n"
        f"⚡️Учета доходов, расходов и аналитики \n"
        f"⚡️Добавление в группу/беседу и практически все, что может прийти в голову",
        reply_markup=cost)