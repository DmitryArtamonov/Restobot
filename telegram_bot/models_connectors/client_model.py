from asgiref.sync import sync_to_async
from restobot_api.models import Client


@sync_to_async
def check_and_create_client(telegram_id: int, name:str):
    """
    Check if client exists by telegram ID. If not, create new client.
    :return: client id
    """
    try:
        client = Client.objects.filter(telegram_id=telegram_id)
        if client:
            id = client[0].id
            print(f'client found in database, id:{id}, telegram_id:{telegram_id}')
            return id

        else:
            new_client = Client()
            new_client.telegram_id = telegram_id
            new_client.name = name
            new_client.save()
            print(f' new client created in database, id:{new_client.id}, telegram_id:{telegram_id}')
            return new_client.id

    except Exception as e:
        return f'Error in check/create a client: {e}'


@sync_to_async
def get_client_by_tg_id(telegram_id: int):
    try:
        client = Client.objects.filter(telegram_id=telegram_id)
        if client:
            return client[0]
        else:
            raise (Exception, 'Client not found in DB')

    except Exception as e:
        return f'Error in get_client: {e}'


