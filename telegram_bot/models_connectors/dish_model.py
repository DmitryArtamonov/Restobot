from asgiref.sync import sync_to_async
from django.db.models import Q
from django.forms import model_to_dict

from restobot_api.models import Dish


@sync_to_async
def get_dish(id):
    """
    Find dish by id
    :param id:
    :return: dish
    """
    try:
        dish = Dish.objects.filter(id=id)
        if not dish:
            raise ValueError (f'Dish id{id} not found in Dish model')
        print('Got dish', dish[0])
        print('Dish price:', dish[0].price)
        return dish[0]

    except Exception as e:
        return f'Error in get_dish: {e}'


@sync_to_async
def get_dishes(restaurant_id: int, group: str):
    """
    Find dishes by restaurant and group
    :param restaurant_id:
    :param group:
    :return: list of dishes as dict
    """
    dishes_query = Dish.objects.filter(Q(restaurant=restaurant_id) & Q(group__name=group))
    dishes = [model_to_dict(instance) for instance in dishes_query]
    return dishes
