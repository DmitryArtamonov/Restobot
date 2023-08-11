from asgiref.sync import sync_to_async
from restobot_api.models import Chat
from .client_model import get_client_by_tg_id
from .restaurant_model import get_restaurant


@sync_to_async
def send_message(restaurant_id: int, client_tg_id: int, message: str):
    """
    Add message from client to the model
    :return:
    """
    try:
        new_message = Chat()
        new_message.author = 'c'
        new_message.client = await get_client_by_tg_id(client_tg_id)
        new_message.restaurant = await get_restaurant(restaurant_id)
        new_message.message = message
        new_message.save()

    except Exception as e:
        return f'Error in creating message: {e}'

