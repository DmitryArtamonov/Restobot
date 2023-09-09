from telegram_bot.models_connectors.dish_model import get_dishes
from telegram_bot.models_connectors.group_model import get_groups_with_items

class Restaraunt:

    def __init__(self, restaurant_id, telegram_token):

        self.id = restaurant_id
        self.token = telegram_token

    async def get_groups(self):
        return await get_groups_with_items(restaurant_id=self.id)

    async def get_dishes(self, group: str):
        return await get_dishes(restaurant_id=self.id, group=group)



