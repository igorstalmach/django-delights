from django.db import models
from django.utils import timezone


UNIT_CHOICES = [
        ("kg", "kg"),
        ("dag", "dag"),
        ("g", "g"),
        ("pcs", "pcs"),
    ]


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(choices=UNIT_CHOICES, default="g", max_length=3)
    price_per_unit = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.name}, Qty {self.quantity} {self.unit}, Per unit: ${self.price_per_unit}"

    def get_absolute_url(self):
        return "/ingredients"



class Recipe(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.name}, ${self.price}"

    def get_absolute_url(self):
        return "/recipes"


class RecipeRequirement(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(choices=UNIT_CHOICES, default="g", max_length=3)

    def __str__(self):
        return f"{self.ingredient.name} required for {self.recipe.name}, Qty {self.quantity} {self.unit}"

    def get_absolute_url(self):
        return "/requirements"


class Purchase(models.Model):
    item = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.item.name} at {self.date}"

    def get_absolute_url(self):
        return "/purchases"
