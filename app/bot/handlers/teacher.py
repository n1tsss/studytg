from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.filters.role import RoleFilter

router = Router(name='teacher')


@router.message(Command('teacher'), RoleFilter('teacher'))
async def teacher_panel(message: Message) -> None:
    await message.answer('Режим преподавателя: создание событий и выставление баллов.')
