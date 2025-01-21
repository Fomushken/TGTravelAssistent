from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from states.main_states import FSMMenu, FSMTravel
from lexicon.lexicon_ru import BUTTONS_LEXICON, ANSWERS_LEXICON
from keyboards.travel_keyboards import currency_kb, travel_kb

router = Router()

@router.message(StateFilter(FSMMenu.on_travel), F.text == BUTTONS_LEXICON['currency_btn'])
async def currency_enter_handler(message: Message, state: FSMContext):
    await state.set_state(FSMTravel.currency_first)
    await message.answer(text=ANSWERS_LEXICON['currency_btn'], reply_markup=currency_kb)

@router.message(StateFilter(FSMTravel.currency_first))
async def first_currency_handler(message: Message, state: FSMContext):
    await state.set_state(FSMTravel.currency_amount)
    await message.answer(text=ANSWERS_LEXICON['amount_currency'])

@router.callback_query(StateFilter(FSMTravel.currency_first))
async def first_currency_callback_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMTravel.currency_amount)
    print(callback.data)
    await callback.message.delete()
    await callback.message.answer(text=ANSWERS_LEXICON['amount_currency'])


@router.message(StateFilter(FSMTravel.currency_amount))
async def amount_currency_handler(message: Message, state: FSMContext):
    await state.set_state(FSMTravel.currency_second)
    await message.answer(text=ANSWERS_LEXICON['second_currency'], reply_markup=currency_kb)

@router.message(StateFilter(FSMTravel.currency_second))
async def second_currency_handler(message: Message, state: FSMContext):
    await state.set_state(FSMTravel.currency_result_end)
    await message.answer(text=ANSWERS_LEXICON['result_currency'].format('dick', 'dickk', 'dickkk', 'dickkkk'), reply_markup=travel_kb)

@router.callback_query(StateFilter(FSMTravel.currency_second))
async def first_currency_callback_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMTravel.currency_result_end)
    print(callback.data)
    await callback.message.delete()
    await callback.message.answer(text=ANSWERS_LEXICON['result_currency'].format('dick', 'dickk', 'dickkk', 'dickkkk'), reply_markup=travel_kb)

