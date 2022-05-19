from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import info_callback, start_callback

start_info = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Создание сайтов",
                                          callback_data=info_callback.new(item_name='site',
                                                                          link='Подробнее')
                                      ),
                                      InlineKeyboardButton(
                                          text="Создание ботов",
                                          callback_data="info:develop:Подробнее"
                                      )
                                  ]
                                  ])
siteToBot = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Создание ботов",
                                          callback_data="info:develop:Подробнее"
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
                                       text="Как же создаются телеграм боты?",
                                       callback_data=info_callback.new(item_name='techno',
                                                                       link='Подробнее')
                                   )
                               ]
                               ])

examples = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[[
                                   InlineKeyboardButton(
                                       text="Где я могу применить боты?",
                                       callback_data=info_callback.new(item_name='examples',
                                                                       link='Подробнее')
                                   )
                               ]
                               ])


cost = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[[
                                   InlineKeyboardButton(
                                       text="Сколько же это стоит?",
                                       callback_data=info_callback.new(item_name='price',
                                                                       link='Подробнее')
                                   )
                               ]
                               ])

connect = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Свяжитесь со мной",
                                          callback_data="info:contacts:Подробнее"
                                      )
                                  ]
                              ])
