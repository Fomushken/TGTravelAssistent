from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.main_states import FSMMenu
from lexicon.lexicon_ru import BUTTONS_LEXICON, ANSWERS_LEXICON
from keyboards.travel_keyboards import travel_kb

router = Router()

@router.message(StateFilter(FSMMenu.main_menu_start), F.text == BUTTONS_LEXICON["travel_btn"])
async def travel_btn_handler(message: Message, state: FSMContext):
    await state.set_state(FSMMenu.on_travel)
    await message.answer(text=ANSWERS_LEXICON["travel_btn"], reply_markup=travel_kb)

@router.message(StateFilter(FSMMenu.main_menu_start), F.text == BUTTONS_LEXICON["tasks_btn"])
async def tasks_btn_handler(message: Message, state: FSMContext):
    await message.answer(text=ANSWERS_LEXICON["tasks_btn"])

@router.message(StateFilter(FSMMenu.main_menu_start), F.text == BUTTONS_LEXICON["daily_btn"])
async def daily_btn_handler(message: Message, state: FSMContext):
    await message.answer(text=ANSWERS_LEXICON["daily_btn"])
#
# @router.message(StateFilter(FSMMenu.main_menu_start), F.text == BUTTONS_LEXICON["back_btn"])
# async def back_btn_handler(message: Message, state: FSMContext):
#     # await state.set_state()
#     await message.answer(text=ANSWERS_LEXICON["back_btn"])