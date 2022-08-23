from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("ingredients/", views.ViewIngredients.as_view(), name="ingredients"),
    path("ingredients/add_ingredient", views.AddIngredient.as_view(), name="add_ingredient"),
    path("purchases/", views.ViewPurchase.as_view(), name="purchases"),
    path("purchases/add_purchase/", views.AddPurchase.as_view(), name="add_purchase"),
    path("recipes/", views.ViewRecipe.as_view(), name="recipes"),
    path("recipes/add_recipe/", views.AddRecipe.as_view(), name="add_recipe"),
    path("recipes/add_recipe_requirement/", views.AddRecipeRequirement.as_view(), name="add_recipe_req"),
]