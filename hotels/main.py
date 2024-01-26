from hotels import app

from fastapi.staticfiles import StaticFiles

from hotels.bookings.router import router as booking_router
from hotels.config import REDIS_HOST, REDIS_PORT
from hotels.users.router import router as auth_router
from hotels.hotels.router import router as hotels_router
from hotels.pages.router import router as pages_router
from hotels.images.router import router as images_router

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

app.mount('/static', StaticFiles(directory='hotels/static'), 'static')

app.include_router(auth_router)
app.include_router(booking_router)
app.include_router(hotels_router)
app.include_router(pages_router)
app.include_router(images_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
