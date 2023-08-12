import aiogram
import asyncio
from telegram_bot.models_connectors.chat_model import check_new_messages, mark_message_not_new


async def message_listener(bot: aiogram.Bot):
    """
    Check for new messages from restaurants and print them
    :return:
    """
    check_interval = 1000  # check new message every ... sec
    message_interval = 0.1 # send new message every ... sec (not to break TG limits if there are a lot of msgs)
    error_interval = 0.1 # Delay in seconds between retries if there is an error
    print('Start message listener')
    while True:
        await asyncio.sleep(check_interval)
        print("checking for new messages")
        try:
            new_messages = await check_new_messages()
            print(f'found {len(new_messages)} new messages')
            for message in new_messages:
                await bot.send_message(message[1], f'💬 {message[2]} 💬')  # send message to client
                await mark_message_not_new(message[0])  # remove 'is_new' mark
                await asyncio.sleep(message_interval)

        except Exception as e:
            print(f'Error new messages listener: {e}')
            await asyncio.sleep(error_interval)


