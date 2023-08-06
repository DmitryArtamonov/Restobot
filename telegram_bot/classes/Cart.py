from functools import reduce
from restobot_api.models import Dish
from asgiref.sync import sync_to_async

class Cart():

    def __init__(self):
        self.items = []


    # get amount of item in cart by dish ID
    def get_item_amount(self, dish_id: int):

        filtered = filter(lambda x: x['id'] == dish_id, self.items) # filtering by id
        amount = reduce(lambda acc, y: acc + y['amount'], filtered, 0)   # sum of amounts

        return amount

    # edit amount of items in cart, create new cart item if added first time, remove if amount become 0
    @sync_to_async
    def edit_item(self, dish_id: int, amount: int):
        print('edit_item started', 'id', dish_id, 'amount', amount)
        try:
            # if same item with same price already in cart, add amount
            price = Dish.objects.filter(id=dish_id)[0].price # Temporaly. Later different prices for the same item can be added.
            for index, item in enumerate(self.items):
                if item['id'] == dish_id and item['price'] == price:
                    item['amount'] = item['amount'] + amount

                    # if amount become 0 or less - remove item from the cart
                    if item['amount'] <= 0:
                        del self.items[index]
                        item['amount'] = 0

                    print('item changed in a cart', item)
                    return item

            # if not in cart and amount <=0
            if amount <= 0:
                return {'amount': 0}

            # else: add to cart
            dish = Dish.objects.filter(id=dish_id)[0] # get dish info from the model
            new_item = {'id': dish_id, 'name': dish.name, 'amount': amount, 'price': dish.price, 'value': amount * dish.price}
            self.items.append(new_item)
            print('new item in a cart', new_item)
            return new_item

        except Exception as e:
            print("Error in cart:", str(e))
            return(f'Error in cart: {str(e)}')

