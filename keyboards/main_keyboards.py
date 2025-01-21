from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import BUTTONS_LEXICON

# General buttons(used multiple times)
back_btn = KeyboardButton(text=BUTTONS_LEXICON["back_btn"])

# Main menu keyboard
travel_btn = KeyboardButton(text=BUTTONS_LEXICON["travel_btn"])
tasks_btn = KeyboardButton(text=BUTTONS_LEXICON["tasks_btn"])
daily_btn = KeyboardButton(text=BUTTONS_LEXICON["daily_btn"])
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [travel_btn, tasks_btn],
        [daily_btn],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Help menu keyboard

developer_btn = KeyboardButton(text=BUTTONS_LEXICON["developer_btn"])
instruction_btn = KeyboardButton(text=BUTTONS_LEXICON["instruction_btn"])
help_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [developer_btn, instruction_btn],
        [back_btn],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)