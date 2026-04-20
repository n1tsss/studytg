from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.filters.role import RoleFilter

router = Router(name='leader')


@router.message(Command('leader'), RoleFilter('leader'))
async def leader_panel(message: Message) -> None:
    await message.answer('Распределение делегированного среднего балла.')
