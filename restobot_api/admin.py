from django.contrib import admin
from .models import Dish, Restaurant, Category, Group, Client, Order, Order_item, Chat

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Chat)
