from restobot_api.models import Dish
from restobot_api.models import Group
from restobot_api.serializers import DishSerializer
from asgiref.sync import sync_to_async
from django.db.models import Q
from django.forms.models import model_to_dict

class Restaraunt:

    def __init__(self, restaurant_id, telegram_token):

        self.id = restaurant_id
        self.token = telegram_token

    @sync_to_async
    def get_groups(self):
        groups = Group.objects.filter(restaurant=self.id)

        return [str(s) for s in groups]


    @sync_to_async
    def get_dishes(self, group: str):
        dishes_query = Dish.objects.filter(Q(restaurant=self.id) & Q(group__name=group))
        dishes = [model_to_dict(instance) for instance in dishes_query]
        return dishes



