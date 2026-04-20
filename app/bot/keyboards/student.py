from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def student_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='/student')], [KeyboardButton(text='/leader')]],
        resize_keyboard=True,
    )
