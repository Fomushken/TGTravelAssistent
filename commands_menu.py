import logging

from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon_ru import COMMANDS_MENU

async def set_main_menu(bot: Bot):
    try:
        main_menu_commands = [
            BotCommand(command=command,
                       description=description
                       ) for command, description in COMMANDS_MENU.items()
        ]
        await bot.set_my_commands(main_menu_commands)
        logging.info("Menu set successfully")
    except Exception as e:
        logging.error(e)