from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def dish_keyboard(dish_id: int, amount: int):
    """
    Create an inline keyboard under the dish photo to change amount: [-]...0...[+]
    :param dish_id: id of the item(dish)
    :param amount: current amount in the cart
    :return: inline keyboard
    """

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
