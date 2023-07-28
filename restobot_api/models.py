from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    tg_token = models.CharField(max_length=100)

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
    picture = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

