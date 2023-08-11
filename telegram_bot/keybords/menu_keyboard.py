from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from .buttons import home_button


def menu_keyboard(categories: list[str]):
    """
    Create and return outline menu at the bottom of the screen with menu categories and additional buttons
    :param categories: list of categories
    :return: inline keyboard
    """

    builder = ReplyKeyboardBuilder()

    for category in categories:
        builder.add(KeyboardButton(text=category))
    builder.add(home_button)
    builder.add(KeyboardButton(text="🛒 Cart"))

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)
