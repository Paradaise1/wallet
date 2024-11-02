from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from api.router import router as api_router
from config import REDIS_HOST, REDIS_PORT
from database import Base, engine


app = FastAPI(title='Wallet')
app.include_router(api_router)


@app.on_event('startup')
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    redis = aioredis.from_url(
        f'redis://{REDIS_HOST}:{REDIS_PORT}',
        encoding='utf8',
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
