from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback, start_callback
from keyboards.inline.choice_buttons import siteToBot
from loader import dp, bot
from app import BotDB

SITE_LINK = "https://selection-studio.com/"


@dp.callback_query_handler(info_callback.filter(item_name="site"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.message.answer(f"Согласись, что про сайты лучше смотреть на самом сайте?🌚\n \n"
                              f"Поэтому вот ссылка, там сразу есть вся нужная информация: {SITE_LINK} \n")
    await call.message.answer(f"⬇️Если хочешь почитать про ботов, жми⬇️",
                              reply_markup=siteToBot)


@dp.callback_query_handler(info_callback.filter(item_name="contacts"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer("Спасибо, наш представитель скоро свяжется с Вами", show_alert=True)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("Вы отменили получение информации", show_alert=True)
    await call.message.edit_reply_markup()
