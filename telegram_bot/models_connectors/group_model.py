from asgiref.sync import sync_to_async
from restobot_api.models import Group
from .dish_model import get_dishes_sync
from django.db import close_old_connections


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
        close_old_connections()
        return f'Error in get groups: {e}'


@sync_to_async
def get_groups_with_items(restaurant_id: int):
    """
    Find not empty groups by restaurant
    :return: list of goups names
    """
    try:
        groups = Group.objects.filter(restaurant=restaurant_id)
        group_names = map(lambda grp: str(grp), groups)  # get names of groups
        groups_with_items = list(filter(
            lambda grp: get_dishes_sync(restaurant_id=restaurant_id, group=grp),
            group_names)
        )  # filter not empty groups

        return groups_with_items

    except Exception as e:
        close_old_connections()
        return f'Error in get groups: {e}'
