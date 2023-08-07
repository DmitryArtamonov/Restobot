from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def order_place_button():
    """
    Create an inline button for order placement
    :return:
    """
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="✔️ Place Order!",
        callback_data='order_place'))
    return builder.as_markup()