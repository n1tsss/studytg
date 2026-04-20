from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def teacher_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='/teacher')]],
        resize_keyboard=True,
    )
