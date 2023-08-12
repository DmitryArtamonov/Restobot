from .models import Restaurant, Dish, Group, Order, Client, Chat, Order_item
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'restaurant', 'name')


class DishSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    group_name = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = Dish
        fields = ('id', 'name', 'restaurant', 'description', 'picture', 'price', 'group_name', 'group', 'categories')

    def get_group_name(self, obj):
        return obj.group.name if obj.group else None

    def get_group(self, obj):
        return GroupSerializer(obj.group.all()).data


class DishCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ('name', 'restaurant', 'description', 'picture', 'price', 'group', 'categories')


class DishDeleteSerializer(serializers.Serializer):
    class Meta:
        pass


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = ('id', 'dish', 'dish_name', 'amount', 'price')


class OrderSerializer(serializers.ModelSerializer):
    creation_time = serializers.DateTimeField(format='%d.%m.%y %H:%M')
    items = OrderItemSerializer(many=True, read_only=True)
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'number',
            'client',
            'client_name',
            'restaurant',
            'delivery_address',
            'phone_number',
            'comments',
            'creation_time',
            'status',
            'value',
            'items'  # Include the items field here
        )
        ordering = ['-id']

    def get_client_name(self, obj):
        return obj.client.name if obj.client else None


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status',)
