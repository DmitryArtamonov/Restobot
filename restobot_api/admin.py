from django.contrib import admin
from .models import Dish, Restaurant, Category, Group

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Dish)