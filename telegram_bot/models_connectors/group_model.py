from asgiref.sync import sync_to_async
from restobot_api.models import Group


@sync_to_async
def get_groups(restaurant_id: int):
    """
    Find groups by restaurant
    :return: list of goups names
    """
    try:
        groups = Group.objects.filter(restaurant=restaurant_id)

        return [str(s) for s in groups]

    except Exception as e:
        return f'Error in get groups: {e}'

