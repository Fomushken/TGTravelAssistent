from aiogram.fsm.state import State, StatesGroup

class FSMHelp(StatesGroup):
    help_menu = State()
    developer_message = State()
    instruction = State()