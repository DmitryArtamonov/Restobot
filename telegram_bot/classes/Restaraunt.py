from restobot_api.models import Group
from asgiref.sync import sync_to_async
from telegram_bot.models_connectors.dish_model import get_dishes
from telegram_bot.models_connectors.group_model import get_groups

class Restaraunt:

    def __init__(self, restaurant_id, telegram_token):

        self.id = restaurant_id
        self.token = telegram_token

    async def get_groups(self):
        return await get_groups(restaurant_id=self.id)

    async def get_dishes(self, group: str):
        return await get_dishes(restaurant_id=self.id, group=group)



