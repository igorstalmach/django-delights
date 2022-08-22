from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient, Recipe, RecipeRequirement, Purchase


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        context['recipes'] = Recipe.objects.all()
        context['purchases'] = Purchase.objects.all()
        return context