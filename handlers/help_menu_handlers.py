from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.help_menu_states import FSMHelp
from states.main_states import FSMMenu
from lexicon.lexicon_ru import BUTTONS_LEXICON, ANSWERS_LEXICON
from keyboards.main_keyboards import help_keyboard, main_keyboard

router = Router()

@router.message(StateFilter(FSMHelp.help_menu), F.text == BUTTONS_LEXICON["instruction_btn"])
async def instruction_handler(message: Message, state: FSMContext):
    await message.answer(text=ANSWERS_LEXICON["instruction_btn"], reply_markup=help_keyboard)

@router.message(StateFilter(FSMHelp.help_menu), F.text == BUTTONS_LEXICON["developer_btn"])
async def contact_dev_handler(message: Message, state: FSMContext):
    await state.set_state(FSMHelp.developer_message)
    await message.answer(text=ANSWERS_LEXICON["developer_btn"])

@router.message(StateFilter(FSMHelp.developer_message))
async def developer_message_handler(message: Message, state: FSMContext):
    message_to_the_dev = (f"Message from user: @{message.from_user.username or 'No name'} (ID: {message.from_user.id})\n\n"
                          f"Message text: {message.text}")
    await message.bot.send_message(chat_id=940933457, text=message_to_the_dev)
    # await message.send_copy(chat_id=940933457)
    await state.set_state(FSMHelp.help_menu)
    await message.answer(text=ANSWERS_LEXICON["developer_message_sent"], reply_markup=help_keyboard)

@router.message(StateFilter(FSMHelp.help_menu), F.text == BUTTONS_LEXICON["back_btn"])
async def back_button_handler(message: Message, state: FSMContext):
    await state.set_state(FSMMenu.main_menu_start)
    await message.answer(text=ANSWERS_LEXICON["back_btn"], reply_markup=main_keyboard)