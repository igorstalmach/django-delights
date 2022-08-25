from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("logged-out/", views.log_out_view, name="logout_view"),
    path("sign-up/", views.SignUpView.as_view(), name="signup"),
    path("ingredients/", views.ViewIngredients.as_view(), name="ingredients"),
    path("ingredients/add-ingredient/", views.AddIngredient.as_view(), name="add_ingredient"),
    path("ingredients/<pk>/update-ingredient/", views.UpdateIngredient.as_view(), name="update_ingredient"),
    path("ingredients/<pk>/delete-ingredient/", views.DeleteIngredient.as_view(), name="delete_ingredient"),
    path("purchases/", views.ViewPurchase.as_view(), name="purchases"),
    path("purchases/add-purchase/", views.AddPurchase.as_view(), name="add_purchase"),
    path("purchases/<pk>/update-purchase/", views.UpdatePurchase.as_view(), name="update_purchase"),
    path("purchases/<pk>/delete-purchase", views.DeletePurchase.as_view(), name="delete_purchase"),
    path("recipes/", views.ViewRecipe.as_view(), name="recipes"),
    path("recipes/add-recipe/", views.AddRecipe.as_view(), name="add_recipe"),
    path("recipes/<pk>/update-recipe/", views.UpdateRecipe.as_view(), name="update_recipe"),
    path("recipes/<pk>/delete-recipe/", views.DeleteRecipe.as_view(), name="delete_recipe"),
    path("recipes/add-recipe-requirement/", views.AddRecipeRequirement.as_view(), name="add_recipe_req"),
    path("recipes/<pk>/update-recipe-requirement/", views.UpdateRecipeRequirement.as_view(), name="update_recipe_req"),
    path("recipes/<pk>/delete-recipe-requirement/", views.DeleteRecipeRequirement.as_view(), name="delete_recipe_req"),
]
