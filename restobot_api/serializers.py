from .models import Restaurant, Dish, Group
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class DishSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Dish
        fields = ('id', 'name', 'restaurant', 'description', 'picture', 'price', 'group', 'categories')

    def get_group(self, obj):
        return GroupSerializer(obj.group.all()).data