from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot

from app.infrastructure.scheduler.jobs import register_jobs


def build_scheduler(_: Bot) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    register_jobs(scheduler)
    return scheduler
