from keyboards.inline.callback_datas import info_callback
from keyboards.inline.choice_buttons import choice, botInfo, technology, cost, examples, connect
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(info_callback.filter(item_name="develop"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Чат-бот — это автоматизированный многофункциональный помощник, который может показывать информацию подписчикам и собирать информацию по запросу согласно заранее подготовленным сценариям. ",
        reply_markup=botInfo)


@dp.callback_query_handler(info_callback.filter(item_name="botPluses"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f" ⏰ Мгновенные ответы на сообщения  \n"
        f" 🌎 Доступность с любых устройств по всему миру  \n"
        f" 🌚 Конфиденциальность сообщений  \n"
        f" 💰 Автоматизация всех процессов, в том числе оплаты ",
        reply_markup=technology)


@dp.callback_query_handler(info_callback.filter(item_name="techno"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"В процессе разработки мы используем Python - один из самых популярных и востребованных языков в мире.\n"
        f"Мы НЕ работаем на готовых конструкторах, а подходим индивидуально к каждому проекту",
        reply_markup=examples)


@dp.callback_query_handler(info_callback.filter(item_name="examples"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Бот для оптимизации продаж \n"
        f"Для рассылки сообщений \n"
        f"Учета доходов, расходов и аналитики \n"
        f"Добавление в группу/беседу и др.",
        reply_markup=cost)


@dp.callback_query_handler(info_callback.filter(item_name="price"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Стоимость разработки чат-бота для Telegram от 23.990 рублей. \n"
        f"Все будет зависеть от сложности и сроков, в которые необходимо выполнить.",
        reply_markup=connect)


@dp.callback_query_handler(info_callback.filter(item_name="promo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Введите промокод:")
