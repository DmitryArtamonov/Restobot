from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import (
    Restaurant,
    Group,
    Dish,
    Order
)

from .serializers import (
    RestaurantSerializer,
    GroupSerializer,
    DishSerializer,
    DishCreateSerializer,
    DishDeleteSerializer,
    OrderSerializer,
    OrderStatusUpdateSerializer
)


class DishListView(generics.ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return Dish.objects.filter(restaurant_id=restaurant_id)


class DishDetailView(generics.RetrieveAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()

    def get_object(self):
        dish_id = self.kwargs.get('id')
        return generics.get_object_or_404(Dish, id=dish_id)


class DishCreateView(generics.CreateAPIView):
    serializer_class = DishCreateSerializer
    queryset = Dish.objects.all()
    permission_classes = (AllowAny,)


class DishUpdateView(generics.UpdateAPIView):
    serializer_class = DishCreateSerializer
    queryset = Dish.objects.all()
    permission_classes = (AllowAny,)

    def get_object(self):
        dish_id = self.kwargs.get('id')
        return generics.get_object_or_404(Dish, id=dish_id)


class DishDeleteView(generics.DestroyAPIView):
    serializer_class = DishDeleteSerializer
    queryset = Dish.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class OrdersListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        return Order.objects.order_by('-id')


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusUpdateSerializer
    permission_classes = (AllowAny,)

    # def put(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #
    #     # Serialize the request data, but only update the provided fields
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     return Response(serializer.data)