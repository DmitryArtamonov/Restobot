from django.urls import path, include

from .views import (
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    GroupListView,
    GroupCreateView,
    OrdersListView,
    OrderDetailView,
    OrderUpdateView,
    run_bot
)

urlpatterns = [
    path('dishes/<int:restaurant_id>', DishListView.as_view(), name='dish_list_api'),
    path('dish/new', DishCreateView.as_view(), name='dish_create_api'),
    path('dish/update/<int:id>', DishUpdateView.as_view(), name='dish_update_api'),
    path('dish/delete/<int:id>', DishDeleteView.as_view(), name='dish_delete_api'),
    path('dish/get/<int:id>', DishDetailView.as_view(), name='dish_detail_api'),
    path('groups/new', GroupCreateView.as_view(), name='group_create_api'),
    path('groups/<int:restaurant_id>', GroupListView.as_view(), name='group_list_api'),
    path('orders/<int:restaurant_id>', OrdersListView.as_view(), name='order_list_api'),
    path('order/get/<int:pk>', OrderDetailView.as_view(), name='order_detail_api'),
    path('order/update/<int:pk>', OrderUpdateView.as_view(), name='order_update_api'),
    path('run-bot/', run_bot, name='run_bot'),
]

