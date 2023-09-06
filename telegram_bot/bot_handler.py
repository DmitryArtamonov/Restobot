import asyncio
from .utils import clean_string
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, CallbackQuery, InputMediaPhoto
from aiogram.filters.command import Command as aiCommand
from telegram_bot.keybords.order_button import order_button
from telegram_bot.keybords.order_place_button import order_place_button
from telegram_bot.classes.User import User
from restobot_api.utils.config_reader import config
from telegram_bot.classes.Restaraunt import Restaraunt

from telegram_bot.models_connectors.chat_model import send_message
from telegram_bot.keybords.dish_keyboard import dish_keyboard
from telegram_bot.keybords.menu_keyboard import menu_keyboard
from telegram_bot.keybords.home_keyboard import home_keyboard
from telegram_bot.keybords.buttons import home_text, cart_text, menu_text, chat_text

from .message_listener import message_listener
from boto.s3.connection import S3Connection
import os

print('BOT_TOKEN', os.environ['BOT_TOKEN'])

# if 'bot_token' in os.environ:
#     bot_token = S3Connection(os.environ['bot_token'])
# else:
#     bot_token = config.bot_token.get_secret_value()

bot_token = os.environ['BOT_TOKEN']

bot = Bot(token=bot_token, parse_mode="HTML")
dp = Dispatcher()
restaurant = Restaraunt(1, 'aaa')




# Setting States
class FSMFillForm(StatesGroup):
    home = State()
    menu = State()
    chat = State()
    order_name = State()
    order_tel = State()
    order_address = State()
    order_comments = State()
    order_placement = State()


# Handling command /start
@dp.message(aiCommand("start"))
async def cmd_start(msg: types.Message, state: FSMContext):
    print('smbd said /start')
    await state.clear()
    User.new_user(msg.from_user.id)
    keyboard = home_keyboard()

    await msg.answer(
        "Welcome to our restaurant!",
        reply_markup=keyboard
    )
    await state.set_state(FSMFillForm.home)
    print('set state Home')


# Handling "Home" button
@dp.message(F.text == home_text)
async def back_home(msg: types.Message, state: FSMContext):
    """Back to Homepage"""
    await state.set_state(FSMFillForm.home)
    keyboard = home_keyboard()
    await msg.answer("Homepage", reply_markup=keyboard)


# Handling "Cart" button
@dp.message(F.text == cart_text)
async def cart_page(msg: types.Message, state: FSMContext):
    """Open Cart"""
    await state.set_state(FSMFillForm.menu)
    user = User.new_user(msg.from_user.id)  # get user or create new if not exists
    total_message = None
    user.cart.clean_from_zeros()  # delete elements with zero amount
    cart_print = await user.cart.print()
    for text, keyboard in cart_print:
        total_message = await msg.answer(text, reply_markup=keyboard)
    user.cart.total_message = total_message


# Handling "Menu" button
@dp.message(F.text == menu_text)
async def menu_page(msg: types.Message, state: FSMContext):
    """Open Menu"""
    User.new_user(msg.from_user.id)  # get user or create new if not exists
    groups: list[str] = await restaurant.get_groups()  # get groups
    keyboard = menu_keyboard(groups)
    await msg.answer("Choose group", reply_markup=keyboard)
    await state.set_state(FSMFillForm.menu)
    print('set state Menu')


# Handling "Chat" button
@dp.message(F.text == chat_text)
async def chat_page(msg: types.Message, state: FSMContext):
    """Start Chat"""
    pass
    await state.set_state(FSMFillForm.chat)
    keyboard = home_keyboard()
    await msg.answer("Write your message", reply_markup=keyboard)



# ----- Home State -----

# Handling messages
@dp.message(StateFilter(FSMFillForm.home))
async def home_message_handler(msg: types.Message, state: FSMContext):

    pass


# ----- Chat State -----


@dp.message(StateFilter(FSMFillForm.chat))
async def home_message_handler(msg: types.Message, state: FSMContext):
    await send_message(restaurant_id=restaurant.id, client_tg_id=msg.from_user.id, message=msg.text)
    await msg.answer("We got your message, we'll reply soon")




# ----- Menu State -----

# Handling messages
@dp.message(StateFilter(FSMFillForm.menu))
async def menu_message_handler(msg: types.Message, state: FSMContext):
    print('new message', clean_string(msg.text))
    total_message = None
    user = User.new_user(msg.from_user.id)  # get user or create new if not exists
    groups: list[str] = await restaurant.get_groups()  # get groups

    # Menu groups handler
    if msg.text in groups:
        dishes: list[dict] = await restaurant.get_dishes(msg.text)
        for dish in dishes:
            print('printing dish:', dish['name'])
            image = FSInputFile(f"media/{dish['picture']}")
            text = f"<b>{dish['name']}</b> \n{dish['price']} NIS"

            keyboard = dish_keyboard(dish["id"], user.cart.get_item_amount(dish['id']))

            await msg.answer_photo(
                image, caption=text, reply_markup=keyboard)


# Dish buttons handler

@dp.callback_query(StateFilter(FSMFillForm.menu))
async def dish_button_handler(clbck: CallbackQuery, state: FSMContext):
    user = User.new_user(clbck.from_user.id)
    print('user cart:', user.cart.items)
    data = clbck.data
    print('data', data)
    if 'dish' in data:  # check that one of '+' or '-' buttons pushed
        if 'dish_add' in data:  # button '+' pressed
            change = 1
        else:  # button '-' pressed
            change = -1

        dish_id = int(data.split(':')[1])
        item = await user.cart.edit_item(dish_id, change)  # change amount in the cart and get this amount
        new_amount = item['amount']
        new_keyboard = dish_keyboard(dish_id, new_amount)

        caption_entities = clbck.message.caption_entities

        if clbck.message.photo:  # if the message is picture
            image = InputMediaPhoto(media=clbck.message.photo[0].file_id,
                                    caption=clbck.message.caption,
                                    caption_entities=caption_entities)
            await clbck.message.edit_media(image, reply_markup=new_keyboard)

        else:  # if the message is text
            text, new_keyboard = await user.cart.print_item(dish_id)
            await clbck.message.edit_text(text, reply_markup=new_keyboard)
            new_total_text = await user.cart.print_total()
            if user.cart.total_message:
                await user.cart.total_message.edit_text(new_total_text, reply_markup=order_button())

    elif 'order' in data:
        print('order creation start')
        await clbck.message.answer('Enter your name', reply_markup=home_keyboard())
        await state.set_state(FSMFillForm.order_name)

    await clbck.answer()
    # await bot.edit_message_reply_markup()

# ----- Order-name State -----

@dp.message(StateFilter(FSMFillForm.order_name))
async def input_name(msg: types.Message, state: FSMContext):
    name = msg.text
    user = User.new_user(msg.from_user.id)
    user.cart.name = name
    await msg.answer('Enter your phone number')
    await state.set_state(FSMFillForm.order_tel)


# ----- Order-tel State -----

@dp.message(StateFilter(FSMFillForm.order_tel))
async def input_tel(msg: types.Message, state: FSMContext):
    tel = msg.text
    user = User.new_user(msg.from_user.id)
    user.cart.tel = tel
    await msg.answer('Enter delivery address')
    await state.set_state(FSMFillForm.order_address)


# ----- Order-address State -----

@dp.message(StateFilter(FSMFillForm.order_address))
async def input_address(msg: types.Message, state: FSMContext):
    address = msg.text
    user = User.new_user(msg.from_user.id)
    user.cart.address = address
    await msg.answer('Enter comments')
    await state.set_state(FSMFillForm.order_comments)


# ----- Order-comments State -----

@dp.message(StateFilter(FSMFillForm.order_comments))
async def input_comments(msg: types.Message, state: FSMContext):
    comments = msg.text
    user = User.new_user(msg.from_user.id)
    user.cart.comments = comments
    text = await user.cart.print_order()
    print('order text:', text)
    await msg.answer(text, reply_markup=order_place_button())  # print order info and order button
    await state.set_state(FSMFillForm.order_placement)


# ----- Order-placement State -----

@dp.callback_query(StateFilter(FSMFillForm.order_placement))
async def place_order(clbck: CallbackQuery, state: FSMContext):
    user_id = clbck.from_user.id
    user = User.new_user(user_id)
    if clbck.data == 'order_place':
        await user.cart.order_create(user_id)
        await state.clear()
        keyboard = home_keyboard()
        await clbck.message.answer("Thank you! Your order is sent. We'll answer you soon",
                                   reply_markup=keyboard)






# Start polling
async def main():
    print('Start polling')
    await bot.delete_webhook(drop_pending_updates=True)  # deleting pending messages

    # run polling and message listener in parallel
    polling_task = asyncio.create_task(dp.start_polling(bot))
    message_listener_task = asyncio.create_task(message_listener(bot))
    await asyncio.gather(polling_task, message_listener_task)


def start_bot():
    asyncio.run(main())
