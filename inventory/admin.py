from django.contrib import admin
from .models import Ingredient, Recipe, RecipeRequirement, Purchase

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)