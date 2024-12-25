import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()


class BotConfig:
    def __init__(self):
        self.token = os.getenv("BOT_TOKEN")
        if not self.token:
            raise ValueError("Bot token not set")

        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(bot=self.bot)