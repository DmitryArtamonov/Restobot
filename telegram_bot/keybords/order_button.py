from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def order_button():
    """
    Create an inline button for order placement
    :return:
    """
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="🛍 Order!",
        callback_data='order'))
    return builder.as_markup()