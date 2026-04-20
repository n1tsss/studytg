from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def common_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='/me')], [KeyboardButton(text='/help')]],
        resize_keyboard=True,
    )
