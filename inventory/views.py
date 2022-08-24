from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from .models import Ingredient, Recipe, RecipeRequirement, Purchase
from .forms import IngredientForm, RecipeRequirementForm, RecipeForm, PurchaseForm


@login_required
def log_out(request):
    logout(request)
    return redirect('logout_view')


def log_out_view(request):
    return render(request, 'registration/logout.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


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


class UpdateIngredient(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/update/update_ingredient.html"
    form_class = IngredientForm


class DeleteIngredient(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/delete/delete_confirm.html"
    success_url = reverse_lazy("ingredients")


class ViewPurchase(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/list/list_purchases.html"


class AddPurchase(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/add/add_purchase.html"
    form_class = PurchaseForm


class UpdatePurchase(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/update/update_purchase.html"
    form_class = PurchaseForm


class DeletePurchase(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/delete/delete_confirm.html"
    success_url = reverse_lazy('purchases')


class ViewRecipe(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "inventory/list/list_recipes.html"


class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "inventory/add/add_recipe.html"
    form_class = RecipeForm


class UpdateRecipe(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "inventory/update/update_recipe.html"
    form_class = RecipeForm


class DeleteRecipe(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "inventory/delete/delete_confirm.html"
    success_url = reverse_lazy('recipes')


class AddRecipeRequirement(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/add/add_reciperequirement.html"
    form_class = RecipeRequirementForm


class UpdateRecipeRequirement(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "inventory/update/update_reciperequirement.html"
    form_class = RecipeRequirementForm


class DeleteRecipeRequirement(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "inventory/delete/delete_confirm.html"
    success_url = reverse_lazy('recipes')
