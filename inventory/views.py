from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from .models import Ingredient, Recipe, RecipeRequirement, Purchase
from .forms import IngredientForm, RecipeRequirementForm, RecipeForm, PurchaseForm


def log_out(request):
    logout(request)
    return redirect("/")


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        context['recipes'] = Recipe.objects.all()
        context['purchases'] = Purchase.objects.all()

        revenue = Purchase.objects.aggregate(revenue=Sum('item__price'))['revenue']
        costs = Ingredient.objects.aggregate(costs=Sum('price_per_unit'))['costs']

        context['revenue'] = revenue
        context['costs'] = costs
        context['profit'] = revenue - costs
        
        return context


class ViewIngredients(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/list/list_ingredients.html"


class AddIngredient(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add/add_ingredient.html"
    form_class = IngredientForm


class ViewPurchase(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/list/list_purchases.html"


class AddPurchase(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/add/add_purchase.html"
    form_class = PurchaseForm


class ViewRecipe(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "inventory/list/list_recipes.html"


class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "inventory/add/add_recipe.html"
    form_class = RecipeForm


class AddRecipeRequirement(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/add/add_reciperequirement.html"
    form_class = RecipeRequirementForm