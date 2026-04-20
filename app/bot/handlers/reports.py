from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='reports')


@router.message(Command('report'))
async def report(message: Message) -> None:
    await message.answer('Отчёт будет сформирован и отправлен администратору.')
