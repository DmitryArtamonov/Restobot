from telegram_bot.classes.Cart import Cart

class User:

    Users = []

    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.cart = Cart()


    '''
    Get id and check if user exists. If not create a new user and add to the Users list. Return existing or new user.
    '''
    @classmethod
    def new_user(cls, telegram_id):
        existing = cls.get_user(telegram_id)
        if existing:
            print('user already exist', telegram_id, cls.Users)
            return existing

        new = User(telegram_id)
        cls.Users.append(new)
        print('created new user:', telegram_id, cls.Users)
        return new


    '''
    Get id, check if the user exists. If yes, return the user. If not return None.
    '''
    @classmethod
    def get_user(cls, telegram_id):
        user_by_id = list(filter(lambda user: user.telegram_id == telegram_id, cls.Users))
        if user_by_id:
            return user_by_id[0]
        print('user not found')
        return

