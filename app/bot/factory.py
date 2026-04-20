from aiogram import Bot, Dispatcher

from app.bot.handlers.admin import router as admin_router
from app.bot.handlers.common import router as common_router
from app.bot.handlers.leader import router as leader_router
from app.bot.handlers.reports import router as reports_router
from app.bot.handlers.student import router as student_router
from app.bot.handlers.teacher import router as teacher_router
from app.bot.middlewares.auth import AuthMiddleware
from app.bot.middlewares.role_guard import RoleGuardMiddleware
from app.bot.middlewares.throttling import ThrottlingMiddleware


def create_bot_stack(token: str) -> tuple[Bot, Dispatcher]:
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.message.middleware(AuthMiddleware())
    dp.message.middleware(RoleGuardMiddleware())
    dp.message.middleware(ThrottlingMiddleware())

    dp.include_router(common_router)
    dp.include_router(admin_router)
    dp.include_router(teacher_router)
    dp.include_router(student_router)
    dp.include_router(leader_router)
    dp.include_router(reports_router)
    return bot, dp
