import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.filters.command import Command as aiCommand
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async

class Command(BaseCommand):
    def handle(self, *args, **options):
        from restobot_api.models import Group
        from .config_reader import config
        from .restaraunt import Restaraunt

        self.stdout.write(self.style.SUCCESS('Command executed successfully'))

        # Включаем логирование, чтобы не пропустить важные сообщения
        logging.basicConfig(level=logging.INFO)
        # Объект бота
        bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
        # Диспетчер
        dp = Dispatcher()

        restaurant = Restaraunt(1, 'aaa')

        # Handling command /start
        @dp.message(aiCommand("start"))
        async def cmd_start(message: types.Message):
            builder = ReplyKeyboardBuilder()
            builder.add(types.KeyboardButton(text='Menu'))
            builder.adjust(2)

            await message.answer(
                "Welcome to our restaurant!",
                reply_markup=builder.as_markup(resize_keyboard=True),
            )


        # Handling messages
        @dp.message()
        async def message_handler(msg: types.Message):

            groups: list[str] = await restaurant.get_groups() #get groups

            if msg.text == 'Menu':
                builder = ReplyKeyboardBuilder()
                for group in groups:
                    builder.add(types.KeyboardButton(text=group))
                builder.add(types.KeyboardButton(text="Back"))

                builder.adjust(2)

                await msg.answer(
                    "Choose group",
                    reply_markup=builder.as_markup(resize_keyboard=True),
                )

            elif msg.text in groups:
                dishes: list[dict] = await restaurant.get_dishes(msg.text)
                for dish in dishes:
                    image = FSInputFile(f"media/{dish['picture']}")
                    text = f"<b>{dish['name']}</b> \n{dish['price']} NIS"
                    print(text)


                    builder = InlineKeyboardBuilder()
                    builder.add(types.InlineKeyboardButton(
                        text="Нажми меня",
                        callback_data=str(dish["id"]))
                    )

                    result_img = await msg.answer_photo(
                        image, caption=text, reply_markup=builder.as_markup())





        # Start polling
        async def main():
            await bot.delete_webhook(drop_pending_updates=True)  # deleting pending messages
            await dp.start_polling(bot)

        asyncio.run(main())
