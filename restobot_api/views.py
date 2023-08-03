from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import (
    Restaurant,
    Group,
    Dish
)

from .serializers import (
    RestaurantSerializer,
    GroupSerializer,
    DishSerializer,
    DishCreateSerializer,
    DishDeleteSerializer
)


class DishListView(generics.ListAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


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
