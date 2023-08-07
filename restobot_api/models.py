from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    tg_token = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# A dish can be in one group and in several categories. Groups is used for admin purposes
# Categories are shown to a client as a menu category.
class Group(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='group')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(default='No_image.jpg', upload_to='dish_pictures/')
    price = models.FloatField()
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, related_name='group')
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.IntegerField(null=True, unique=True)


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('in_delivery', 'In delivery'),
        ('done', 'Done')
    ]

    number = models.CharField(max_length=20)  # number for restaurant, prefix can be added
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    delivery_address = models.CharField(500, null=True, blank=True)
    phone_number = models.CharField(30, null=True, blank=True)
    comments = models.CharField(500, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')


class Order_items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, null=True, on_delete=models.SET_NULL)
    dish_name = models.CharField(max_length=200)
    amount = models.IntegerField()
    price = models.FloatField()