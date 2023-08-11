from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from .buttons import menu_button, cart_button, chat_button


def home_keyboard():
    """
    Create and return menu for homepage
    :param
    :return: outline keyboard
    """

    builder = ReplyKeyboardBuilder()
    builder.add(menu_button)
    builder.add(cart_button)
    builder.add(chat_button)
    builder.adjust(3)

    return builder.as_markup(resize_keyboard=True)
