from django import forms
from .models import Ingredient, Recipe, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'