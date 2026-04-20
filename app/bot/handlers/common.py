from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='common')


@router.message(Command('start'))
async def start(message: Message) -> None:
    await message.answer('Добро пожаловать в систему учений!')


@router.message(Command('help'))
async def help_cmd(message: Message) -> None:
    await message.answer('Доступные команды зависят от вашей роли.')


@router.message(Command('me'))
async def me(message: Message, user_role: str = 'student') -> None:
    await message.answer(f'Ваша роль: {user_role}')
