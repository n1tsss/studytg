from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.filters.role import RoleFilter

router = Router(name='student')


@router.message(Command('student'), RoleFilter('student'))
async def student_panel(message: Message) -> None:
    await message.answer('Ваши баллы и история начислений.')
