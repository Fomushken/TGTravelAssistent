from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import BUTTONS_LEXICON, CALLBACKS_LEXICON

currency_btn = KeyboardButton(text=BUTTONS_LEXICON['currency_btn'])
weather_btn = KeyboardButton(text=BUTTONS_LEXICON['weather_btn'])
back_btn = KeyboardButton(text=BUTTONS_LEXICON['back_btn'])

travel_kb = ReplyKeyboardMarkup(
    keyboard=[
    [currency_btn, weather_btn],
    [back_btn]
],
    resize_keyboard=True,
    one_time_keyboard=True)

usd_btn = InlineKeyboardButton(text=BUTTONS_LEXICON['usd_btn'], callback_data=CALLBACKS_LEXICON['usd_btn'])
eur_btn = InlineKeyboardButton(text=BUTTONS_LEXICON['eur_btn'], callback_data=CALLBACKS_LEXICON['eur_btn'])
rub_btn = InlineKeyboardButton(text=BUTTONS_LEXICON['rub_btn'], callback_data=CALLBACKS_LEXICON['rub_btn'])
cad_btn = InlineKeyboardButton(text=BUTTONS_LEXICON['cad_btn'], callback_data=CALLBACKS_LEXICON['cad_btn'])
back_btn = InlineKeyboardButton(text=BUTTONS_LEXICON['back_btn'], callback_data=CALLBACKS_LEXICON['back_btn'])

currency_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [usd_btn, rub_btn, cad_btn],
        [eur_btn, back_btn]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)