from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    tg_token = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# A dish can be in one group and in several categories. Groups is used for admin purposes
# Categories are shown to a client as a menu category.
class Group(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='group')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='dish_pictures/')
    price = models.FloatField()
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, related_name='group')
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name

