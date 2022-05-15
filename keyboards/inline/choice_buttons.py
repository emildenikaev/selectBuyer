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
                                          text="Создание ботов",
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

botInfo = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[[
                                   InlineKeyboardButton(
                                       text="Основные преимущества ботов:",
                                       callback_data=info_callback.new(item_name='botPluses',
                                                                       link='Подробнее')
                                   )
                               ]
                               ])

technology = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[[
                                   InlineKeyboardButton(
                                       text="Используемые технологии:",
                                       callback_data=info_callback.new(item_name='techno',
                                                                       link='Подробнее')
                                   )
                               ]
                               ])

examples = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[[
                                   InlineKeyboardButton(
                                       text="Могут быть разработаны, например, такие боты:",
                                       callback_data=info_callback.new(item_name='examples',
                                                                       link='Подробнее')
                                   )
                               ]
                               ])


cost = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[[
                                   InlineKeyboardButton(
                                       text="Стоимость:",
                                       callback_data=info_callback.new(item_name='price',
                                                                       link='Подробнее')
                                   )
                               ]
                               ])

connect = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Есть промокод?",
                                          callback_data=info_callback.new(item_name='promo',
                                                                          link='Подробнее')
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Свяжитесь со мной",
                                          callback_data="info:contacts:Подробнее"
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
                                                  text="Продвижение",
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
