from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def home_keyboard():
    """
    Create and return menu for homepage
    :param
    :return: outline keyboard
    """

    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text='Menu'))
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)
