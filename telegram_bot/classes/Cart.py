from functools import reduce
from restobot_api.models import Dish
from asgiref.sync import sync_to_async
from telegram_bot.keybords.dish_keyboard import dish_keyboard

# TODO: Цена товара не должна храниться в Cart, т.к. она может измениться с момента добавления в корзину

class Cart:

    def __init__(self):
        self.items = []

    def get_item_amount(self, dish_id: int):
        """
        Get amount of item in cart by dish ID. It's possible that one dish can be as different objects in a cart.
        :param dish_id:
        :return:
        """

        filtered = filter(lambda x: x['id'] == dish_id, self.items)  # filtering by id
        amount = reduce(lambda acc, y: acc + y['amount'], filtered, 0)  # sum of amounts

        return amount

    @sync_to_async
    def edit_item(self, dish_id: int, amount: int):
        """
        edit amount of items in cart, create new cart item if added first time, remove if amount become 0
        :param dish_id: ID of item(dish)
        :param amount: amount to add (positive or negative)
        :return: item or {amount: int}
        """
        # TODO: унифицировать return (возможно, просто выводить amount как число)

        print('edit_item started', 'id', dish_id, 'amount', amount)
        try:
            # if same item with same price already in cart, add amount
            price = Dish.objects.filter(id=dish_id)[
                0].price  # Temporaly. Later different prices for the same item can be added.
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
            dish = Dish.objects.filter(id=dish_id)[0]  # get dish info from the model
            new_item = {'id': dish_id, 'name': dish.name, 'amount': amount, 'price': dish.price,
                        'value': amount * dish.price}
            self.items.append(new_item)
            print('new item in a cart', new_item)
            return new_item

        except Exception as e:
            print("Error in cart:", str(e))
            return f'Error in cart: {str(e)}'

    def print_item(self, dish_id):
        # Todo: эта фунция подразумевает, что в корзине может быть только одна позиция с каждым товаром.
        # Надо перестроить схему данных в Cart, чтобы это исправить и добавить id позиции в корзине
        """
        Create a text with one item for the cart
        :return: tuple(text, keyboard)
        """
        item = list(filter(lambda x: x['id'] == dish_id, self.items))[0]
        text = f"{item['name']}\n{item['amount']} x {item['price']}: {item['value']} NIS"
        keyboard = dish_keyboard(item['id'], item['amount'])

        return text, keyboard

    def print(self):
        """
        Create a cart page for user (text and buttons)
        :return:
        """

        print(self.items)
        data = []

        for item in self.items:
            text, keyboard = self.print_item(item['id'])
            # text = f"{item['name']}\n{item['amount']} x {item['price']}: {item['value']} NIS"
            # keyboard = dish_keyboard(item['id'], item['amount'])
            data.append((text, keyboard))

        if data:
            total = self.total()
            data.append((f"<b>Total: {total['amount']} items........{total['value']} NIS</b>", None))

        else:
            data.append(("Your cart is empty", None))

        return data

    def total(self):
        """
        Count total amount of items and value of the cart
        :return: {'amount': int, 'value':float}
        """
        amount = reduce(lambda acc, y: acc + y['amount'], self.items, 0)
        value = reduce(lambda acc, y: acc + y['value'], self.items, 0)

        return {'amount': amount, 'value':value}
