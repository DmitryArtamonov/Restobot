from asgiref.sync import sync_to_async
from restobot_api.models import Order, Order_item, Client, Restaurant, Dish
from .restaurant_model import get_restaurant


@sync_to_async
def create_order(cart, user_id):
    """
    Create new order
    :return:
    """

    try:
        client = Client.objects.filter(id=user_id)[0]
        restaurant = get_restaurant(1)
        new_order = Order()
        new_order.number = '100'
        new_order.client = client
        new_order.restaurant = restaurant
        new_order.delivery_address = cart.address
        new_order.phone_number = cart.tel
        new_order.comments = cart.comments
        new_order.status = 'new'
        new_order.value = cart.value

        new_order.save()
        print(f' new order created in database')

        order_id = new_order.id

        for item in cart.items:
            dish = Dish.objects.filter(id=item['id'])[0]
            new_item = Order_item()
            new_item.order = new_order
            new_item.dish = dish
            new_item.dish_name = dish.name
            new_item.amount = item['amount']
            new_item.price = dish.price
            new_item.save()
            print(f'Item {dish.name} added to order {order_id}')


    except Exception as e:
        return f'Error in create an order: {e}'

