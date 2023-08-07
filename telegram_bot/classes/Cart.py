from functools import reduce
from restobot_api.models import Dish
from asgiref.sync import sync_to_async
from telegram_bot.keybords.dish_keyboard import dish_keyboard
from telegram_bot.models_connectors.dish_model import get_dish


class Cart:

    def __init__(self):
        self.items = []

    def get_item_amount(self, dish_id: int):
        """
        Get amount of item in cart by dish ID. It's possible that one dish can be as different objects in a cart.
        :param dish_id:
        :return:
        """
        # TODO: Update the func when data structure of Cart will be updated

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
            for index, item in enumerate(self.items):
                if item['id'] == dish_id:
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
            new_item = {'id': dish_id, 'amount': amount}
            self.items.append(new_item)
            print('new item in a cart', new_item)
            return new_item

        except Exception as e:
            print("Error in cart:", str(e))
            return f'Error in cart: {str(e)}'

    async def print_item(self, dish_id):
        # Todo: эта фунция подразумевает, что в корзине может быть только одна позиция с каждым товаром.
        # Надо перестроить схему данных в Cart, чтобы это исправить и добавить id позиции в корзине
        """
        Create a text with one item for the cart
        :return: tuple(text, keyboard)
        """
        item = list(filter(lambda x: x['id'] == dish_id, self.items))[0]
        dish = await get_dish(dish_id)
        print('Got dish in Cart', dish)
        text = f"{dish.name}\n{item['amount']} x {dish.price}: {item['amount'] * dish.price} NIS"
        keyboard = dish_keyboard(item['id'], item['amount'])

        return text, keyboard

    async def print_total(self):
        """
        Create a message with total amount and value
        :return: str
        """
        total = await self.total()
        return f"<b>Total: {total['amount']} items........{total['value']} NIS</b>"

    async def print(self):
        """
        Create a cart page for user (text and buttons)
        :return:
        """

        print(self.items)
        data = []

        for item in self.items:
            text, keyboard = await self.print_item(item['id'])
            # text = f"{item['name']}\n{item['amount']} x {item['price']}: {item['value']} NIS"
            # keyboard = dish_keyboard(item['id'], item['amount'])
            data.append((text, keyboard))

        if data:
            text = await self.print_total()
            data.append((text, None))

        else:
            data.append(("Your cart is empty", None))

        return data

    async def total(self):
        """
        Count total amount of items and value of the cart
        :return: {'amount': int, 'value':float}
        """

        amount = reduce(lambda acc, y: acc + y['amount'], self.items, 0)

        value = 0
        for item in self.items:
            dish = await get_dish(item['id'])
            value += item['amount'] * dish.price

        return {'amount': amount, 'value': value}
