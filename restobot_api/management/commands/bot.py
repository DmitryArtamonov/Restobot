import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile, CallbackQuery, InputMediaPhoto
from aiogram.filters.command import Command as aiCommand
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        from restobot_api.models import Group
        from telegram_bot.classes.User import User
        from .config_reader import config
        from .restaraunt import Restaraunt
        from telegram_bot.keybords.dish_keyboard import dish_keyboard
        from telegram_bot.keybords.menu_keyboard import menu_keyboard

        self.stdout.write(self.style.SUCCESS('Command executed successfully'))

        bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
        dp = Dispatcher()
        restaurant = Restaraunt(1, 'aaa')

        # Handling command /start
        @dp.message(aiCommand("start"))
        async def cmd_start(msg: types.Message):
            User.new_user(msg.from_user.id)
            builder = ReplyKeyboardBuilder()
            builder.add(types.KeyboardButton(text='Menu'))
            builder.adjust(2)

            await msg.answer(
                "Welcome to our restaurant!",
                reply_markup=builder.as_markup(resize_keyboard=True),
            )

        # Handling messages
        @dp.message()
        async def message_handler(msg: types.Message):
            user = User.new_user(msg.from_user.id)  # get user or create new if not exists
            groups: list[str] = await restaurant.get_groups() #get groups

            # Menu Handler
            if msg.text == 'Menu':
                keyboard = menu_keyboard(groups)
                await msg.answer("Choose group", reply_markup=keyboard)

            # Menu groups handler
            elif msg.text in groups:
                dishes: list[dict] = await restaurant.get_dishes(msg.text)
                for dish in dishes:
                    image = FSInputFile(f"media/{dish['picture']}")
                    text = f"<b>{dish['name']}</b> \n{dish['price']} NIS"

                    keyboard = dish_keyboard(dish["id"], user.cart.get_item_amount(dish['id']))

                    await msg.answer_photo(
                        image, caption=text, reply_markup=keyboard)

            # Cart handler
            elif msg.text == '🛒 Cart':
                cart_print = user.cart.print()
                for text, keyboard in cart_print:
                    await msg.answer(text, reply_markup=keyboard)






        # Dish buttons handler

        @dp.callback_query()
        async def dish_button_handler(clbck: CallbackQuery):
            user = User.new_user(clbck.from_user.id)
            print ('user cart:', user.cart.items)
            data = clbck.data
            print('data', data)
            if 'dish' in data: # check that one of '+' or '-' buttons pushed
                if 'dish_add' in data:  # button '+' pressed
                    change = 1
                else:                   # button '-' pressed
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

                else:   # if the message is text
                    text = clbck.message.text
                    await clbck.message.edit_text(text, reply_markup=new_keyboard)

            await clbck.answer()
            # await bot.edit_message_reply_markup()



        # Start polling
        async def main():
            await bot.delete_webhook(drop_pending_updates=True)  # deleting pending messages
            await dp.start_polling(bot)

        asyncio.run(main())
