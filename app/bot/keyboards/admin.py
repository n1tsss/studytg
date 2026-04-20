from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def admin_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='/admin')], [KeyboardButton(text='/report')]],
        resize_keyboard=True,
    )
