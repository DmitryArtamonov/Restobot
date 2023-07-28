from django.contrib import admin
from .models import Dish, Restaurant, Category

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Dish)