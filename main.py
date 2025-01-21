import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from config import load_config
from handlers.commands_handlers import router as commands_router
from handlers.menu_handlers import router as menu_router
from handlers.help_menu_handlers import router as help_menu_router
from handlers.travel_handlers import router as travel_router
from commands_menu import set_main_menu


async def main() -> None:
    config = load_config()
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    redis = Redis()
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage)
    dp.include_router(commands_router)
    dp.include_router(help_menu_router)
    dp.include_router(menu_router)
    dp.include_router(travel_router)


    await bot.delete_webhook(drop_pending_updates=True)
    await set_main_menu(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    asyncio.run(main())