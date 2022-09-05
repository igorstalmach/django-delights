from django.db import models
from django.utils import timezone, dateformat

UNIT_CHOICES = [
        ("kg", "kg"),
        ("dag", "dag"),
        ("g", "g"),
        ("pcs", "pcs"),
    ]


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(choices=UNIT_CHOICES, default="g", max_length=3)
    price_per_unit = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.name}, Qty {self.quantity} {self.unit}"

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
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.ingredient.name} required for {self.recipe.name}, Qty {self.quantity} {self.ingredient.unit}"

    def get_absolute_url(self):
        return "/recipes"


class Purchase(models.Model):
    item = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=dateformat.format(timezone.now(), 'H:m:s'))
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.item.name} at {self.time}, {self.date}"

    def get_absolute_url(self):
        return "/purchases"
