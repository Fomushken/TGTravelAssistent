import logging
import asyncio
from tkinter.font import names

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from config import BotConfig


# logging
logging.basicConfig(level=logging.INFO)

# bot initialize
config = BotConfig()
bot = config.bot
dp = config.dp

router = Router()

# bot running
async def main():
    # routers register
    dp.include_router(router)

    # run the bot
    await bot.delete_webhook()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
