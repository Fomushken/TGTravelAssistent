from redis.asyncio.client import Redis

redis_client = None

async def get_redis():
    global redis_client
    if redis_client is None:
        redis_client = Redis()
    return redis_client

async def add_first_currency(user_id, currency):
    redis_cli = await get_redis()
    await redis_cli.set(user_id, currency)
