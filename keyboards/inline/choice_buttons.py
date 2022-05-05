from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import info_callback, start_callback

start_info = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Да!",
                                          callback_data=start_callback.new(item_name='yes')
                                      )
                                  ]
                                  ])

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Создание сайтов",
                                          callback_data=info_callback.new(item_name='site',
                                                                          link='Подробнее')
                                      ),
                                      InlineKeyboardButton(
                                          text="Создание телеграмм-ботов",
                                          callback_data="info:telegramm:Подробнее"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      )
                                  ]
                              ])

site_keyboard = InlineKeyboardMarkup()

SITE_LINK = "https://selection-studio.com/"

site_link = InlineKeyboardMarkup(text="Смотри тут", url=SITE_LINK)

site_keyboard.insert(site_link)
