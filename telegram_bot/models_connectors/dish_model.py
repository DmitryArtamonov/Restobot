from asgiref.sync import sync_to_async
from restobot_api.models import Dish


@sync_to_async
def get_dish(id):
    """
    Find dish by id
    :param id:
    :return: dish
    """
    try:
        dish = Dish.objects.filter(id=id)[0]
        if not dish:
            raise ValueError (f'Dish id{id} not found in Dish model')
        print('Got dish', dish)
        print('Dish price:', dish.price)
        return dish

    except Exception as e:
        return f'Error in get_dish: {e}'

