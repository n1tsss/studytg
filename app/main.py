from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.admin import router as admin_router
from app.api.routes.exports import router as exports_router
from app.api.routes.health import router as health_router
from app.api.routes.webhook import router as webhook_router
from app.bot.factory import create_bot_stack
from app.config import get_settings
from app.infrastructure.scheduler.reminder_scheduler import build_scheduler
from app.logging import setup_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    settings = get_settings()
    setup_logging(settings.log_level)

    if not settings.bot_token:
        yield
        return

    bot, dispatcher = create_bot_stack(settings.bot_token)
    scheduler = build_scheduler(bot)
    scheduler.start()
    try:
        yield
    finally:
        scheduler.shutdown(wait=False)
        await dispatcher.storage.close()
        await bot.session.close()


app = FastAPI(title='Military Training Bot', lifespan=lifespan)
app.include_router(health_router)
app.include_router(webhook_router)
app.include_router(admin_router)
app.include_router(exports_router)
