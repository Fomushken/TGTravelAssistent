from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

# @dataclass
# class DBConfig:
#     databate: str
#     db_host: str
#     db_user: str
#     db_password: str
#

@dataclass
class TgBot:
    token: str
    # admin_ids: str


@dataclass
class RedisConfig:
    url: str


@dataclass
class Config:
    tg_bot: TgBot
    # db: DBConfig
    redis: RedisConfig


def load_config() -> Config:

    return Config(
        tg_bot=TgBot(
            token=os.getenv("BOT_TOKEN"),
        ),
        redis = RedisConfig(
            url=os.getenv("REDIS_URL")
        )
    )