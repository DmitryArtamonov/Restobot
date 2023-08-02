from django.urls import path, include

from .views import (
    DishListView,
    DishDetailView,
    DishCreateView,
    GroupListView
)

urlpatterns = [
    path('dishes/<int:restaurant_id>', DishListView.as_view(), name='dish_list_api'),
    path('dish/new', DishCreateView.as_view(), name='dish_create_api'),
    path('dish/<int:id>', DishDetailView.as_view(), name='dish_detail_api'),
    path('groups/<int:restaurant_id>', GroupListView.as_view(), name='group_list_api'),
]

