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
        dish = Dish.objects.filter(id=id)
        if not dish:
            raise ValueError (f'Dish id{id} not found in Dish model')
        print('Got dish', dish[0])
        print('Dish price:', dish[0].price)
        return dish[0]

    except Exception as e:
        return f'Error in get_dish: {e}'

