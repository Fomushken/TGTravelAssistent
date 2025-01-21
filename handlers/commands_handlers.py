from aiogram import Router
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from lexicon import lexicon_ru
from states.main_states import FSMMenu
from states.help_menu_states import FSMHelp

from keyboards.main_keyboards import main_keyboard, help_keyboard

router = Router()

@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.set_state(FSMMenu.main_menu_start)
    await message.answer(text=lexicon_ru.COMMANDS_LEXICON['start'],
                         reply_markup=main_keyboard)

@router.message(Command('help'))
async def help_command(message: Message, state: FSMContext):
    await state.set_state(FSMHelp.help_menu)
    await message.answer(text=lexicon_ru.COMMANDS_LEXICON['help'], reply_markup=help_keyboard)