from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telegram_bot.classes.User import User

'''
Create a keyboard ander the dish photo to change amount: [-]...0...[+]
'''


def dish_keyboard(dish_id: int, amount: int):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="-",
        callback_data=f'dish_rem:{str(dish_id)}'))  # -1ps of dish
    mid_but = builder.add(InlineKeyboardButton(
        text=str(amount),
        callback_data='amount_button'))  # show amount
    print(mid_but.button)
    builder.add(InlineKeyboardButton(
        text="+",
        callback_data=f'dish_add:{str(dish_id)}'))  # +1ps of dish

    return builder.as_markup()
