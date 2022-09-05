from django import forms
from .widgets import DatePickerInput
from .models import Ingredient, Recipe, RecipeRequirement, Purchase


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
        widgets = {
            'date': DatePickerInput(),
            'time': forms.TimeInput(format='%H:%M:%S'),
        }


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'
