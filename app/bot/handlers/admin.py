from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.filters.role import RoleFilter

router = Router(name='admin')


@router.message(Command('admin'), RoleFilter('admin'))
async def admin_panel(message: Message) -> None:
    await message.answer('Панель администратора: сезоны, роли, экспорт, аудит.')
