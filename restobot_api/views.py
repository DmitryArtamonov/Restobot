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
    DishCreateSerializer
)


class DishListView(generics.ListAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class DishDetailView(generics.RetrieveAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class DishCreateView(generics.CreateAPIView):
    serializer_class = DishCreateSerializer
    queryset = Dish.objects.all()
    permission_classes = (AllowAny,)


class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
