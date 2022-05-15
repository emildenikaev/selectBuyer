from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import info_callback, start_callback
from keyboards.inline.choice_buttons import choice, site_keyboard, choiceTelegram, our_skills, startSEO
from loader import dp, bot
from app import BotDB


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
    await call.message.answer("Основные разделы информации:",
                              reply_markup=choiceTelegram)


@dp.callback_query_handler(info_callback.filter(item_name="add"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(f"Контекстная реклама быстрый способ повысить ваши продажи: ")
    await call.message.answer(
        f"Контекстная реклама Яндекс Директ, при грамотной настройке и ведении, позволят получить целевые заявки с вашего сайта уже в день запуска рекламной кампании. Очень важно заказать настройку контекстной рекламы у грамотных и опытных специалистов. От этого будут зависеть затраты на рекламу и успех всей вашей кампании в целом.: ",
        reply_markup=startSEO)


@dp.callback_query_handler(info_callback.filter(item_name="company"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(f"Мы cоздаем продукт, помогающий развивать бизнес: ")
    await call.message.answer(
        f"В основе нашего подхода — глубокий анализ каждого проекта. Мы изучаем компанию и потребности бизнес-задач наших клиентов. Прогнозируем результаты и прибыль клиентов еще на старте сотрудничества.: ",
        reply_markup=our_skills)


@dp.callback_query_handler(info_callback.filter(item_name="startSEOinfo"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("""
     1) Заключаем договор на продвижение ключевых фраз \n
    2) Аудит вашего текстового контента\n
    3) Аудит программного кода\n
    4) Оптимизация всего контента под поиск\n
    5) Создание новых страниц и разделов, если необходимо\n
    6) Копирайтинг / рерайтинг контента под уникальность\n
    7) Работа с внешними факторами продвижения - ссылки\n
    8) Работа с поведенческими факторами, конверсией, отказами
    """)
    await call.message.answer("Основные разделы информации:",
                              reply_markup=choiceTelegram)


@dp.callback_query_handler(info_callback.filter(item_name="skills"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        f"Решаем задачи продвижения бизнеса в интернете. Помогаем выстраивать успешные коммуникации с потребителями и партнерами в digital-среде. В зависимости от ваших потребностей можем реализовать стратегию продвижения с нуля или выполнить отдельные работы в рамках уже утвержденной стратегии.: ")
    await call.message.answer("Основные разделы информации:",
                              reply_markup=choiceTelegram)


@dp.callback_query_handler(info_callback.filter(item_name="contacts"))
async def buying_site(call: CallbackQuery, callback_data: dict):
    await call.answer("Спасибо, наш представитель скоро свяжется с Вами", show_alert=True)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("Вы отменили получение информации", show_alert=True)
    await call.message.edit_reply_markup()
