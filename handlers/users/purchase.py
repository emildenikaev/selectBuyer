from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback, start_callback
from keyboards.inline.choice_buttons import choice, site_keyboard
from loader import dp, bot


@dp.callback_query_handler(start_callback.filter(item_name="yes"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Мы создаем сайты и телеграмм боты,про что хочешь узнать подробнее?",
                              reply_markup=choice)


@dp.callback_query_handler(info_callback.filter(item_name="site"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(f"Подробная информация о создании сайтов: ", reply_markup=site_keyboard)


@dp.callback_query_handler(info_callback.filter(item_name="telegramm"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Информация скоро появится...")


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("Вы отменили получение информации", show_alert=True)
    await call.message.edit_reply_markup()
