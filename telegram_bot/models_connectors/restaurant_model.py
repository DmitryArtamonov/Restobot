from asgiref.sync import sync_to_async
from restobot_api.models import Restaurant


@sync_to_async
def get_restaurant(restaurant_id: int):
    """
    Find groups by restaurant
    :return: list of goups names
    """
    try:
        restaurant = Restaurant.objects.filter(id=restaurant_id)
        if restaurant:
            return restaurant[0]
        else:
            raise (Exception, 'Restaurant not found in DB')

    except Exception as e:
        return f'Error in get restaurant: {e}'

