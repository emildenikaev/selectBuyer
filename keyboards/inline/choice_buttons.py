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

choiceTelegram = InlineKeyboardMarkup(row_width=4,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text="Разработка бота",
                                                  callback_data=info_callback.new(item_name='develop',
                                                                                  link='Подробнее')
                                              ),
                                              InlineKeyboardButton(
                                                  text="Реклама и продвижение",
                                                  callback_data="info:add:Подробнее"
                                              )
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text="Компания",
                                                  callback_data=info_callback.new(item_name='company',
                                                                                  link='Подробнее')
                                              ),
                                              InlineKeyboardButton(
                                                  text="Свяжитесь со мной",
                                                  callback_data="info:contacts:Подробнее"
                                              )
                                          ]
                                      ])

our_skills = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Что мы умеем?",
                                          callback_data=info_callback.new(item_name='skills',
                                                                          link='Подробнее')
                                      )
                                  ]
                                  ])

startSEO = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[[
                                    InlineKeyboardButton(
                                        text="С чего начать SEO продвижение сайта??",
                                        callback_data=info_callback.new(item_name='startSEOinfo',
                                                                        link='Подробнее')
                                    )
                                ]
                                ])

site_keyboard = InlineKeyboardMarkup()

SITE_LINK = "https://selection-studio.com/"

site_link = InlineKeyboardMarkup(text="Смотри тут", url=SITE_LINK)

site_keyboard.insert(site_link)
