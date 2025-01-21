from aiogram.fsm.state import StatesGroup, State

class FSMMenu(StatesGroup):
    main_menu_start = State()
    on_travel = State()
    on_tasks = State()
    on_daily = State()

class FSMTravel(StatesGroup):
    currency_first = State()
    currency_second = State()
    currency_amount = State()
    currency_result_end = State()

    weather_enter = State()
    weather_exit = State()