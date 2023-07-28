from django.urls import path, include

from .views import (
    DishListView,
    DishDetailView
)

urlpatterns = [
    path('dishes/<int:restaurant_id>', DishListView.as_view(), name='dish_list_api'),
    path('dish/<int:id>', DishDetailView.as_view(), name='dish_detail_api')
]

