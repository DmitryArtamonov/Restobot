from django.db.models import Q
from asgiref.sync import sync_to_async
from restobot_api.models import Chat
from .client_model import get_client_by_tg_id
from .restaurant_model import get_restaurant
from django.db import close_old_connections


@sync_to_async()
def check_new_messages():
    """
    Check for new messages from restaurants and return them
    :return: list of lists: [message_id:id, client_tg_id: int, message text: str]
    """
    while True:
        try:
            new_messages_model = Chat.objects.filter(Q(is_new=True) & Q(author='r'))
            new_messages = []
            for message_model in new_messages_model:
                message = [message_model.id, message_model.client.telegram_id, message_model.message]
                new_messages.append(message)

            return new_messages

        except Exception as e:
            print('Error check_new_message', e)
            close_old_connections()
            return e



@sync_to_async()
def mark_message_not_new(message_id):
    """
    Changes message 'is new' to false after successfully sent to client
    :return:
    """
    message = Chat.objects.filter(id=message_id)[0]
    message.is_new = False
    message.save()

async def send_message(restaurant_id: int, client_tg_id: int, message: str):
    """
    Add message from client to the model
    :return:
    """
    @sync_to_async()
    def add_message(restaurant, client, message):
        try:
            new_message = Chat()
            new_message.author = 'c'
            new_message.client = client
            new_message.restaurant = restaurant
            new_message.message = message
            new_message.save()

        except Exception as e:
            return f'Error in creating message: {e}'


    restaurant = await get_restaurant(restaurant_id)
    client = await get_client_by_tg_id(client_tg_id)
    await add_message(restaurant=restaurant, client=client, message=message)

