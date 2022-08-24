from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("logged_out/", views.log_out_view, name="logout_view"),
    path("sign_up/", views.SignUpView.as_view(), name="signup"),
    path("ingredients/", views.ViewIngredients.as_view(), name="ingredients"),
    path("ingredients/add_ingredient/", views.AddIngredient.as_view(), name="add_ingredient"),
    path("ingredients/<pk>/update_ingredient/", views.UpdateIngredient.as_view(), name="update_ingredient"),
    path("ingredients/<pk>/delete_ingredient/", views.DeleteIngredient.as_view(), name="delete_ingredient"),
    path("purchases/", views.ViewPurchase.as_view(), name="purchases"),
    path("purchases/add_purchase/", views.AddPurchase.as_view(), name="add_purchase"),
    path("purchases/<pk>/update_purchase/", views.UpdatePurchase.as_view(), name="update_purchase"),
    path("purchases/<pk>/delete_purchase", views.DeletePurchase.as_view(), name="delete_purchase"),
    path("recipes/", views.ViewRecipe.as_view(), name="recipes"),
    path("recipes/add_recipe/", views.AddRecipe.as_view(), name="add_recipe"),
    path("recipes/<pk>/update_recipe/", views.UpdateRecipe.as_view(), name="update_recipe"),
    path("recipes/<pk>/delete_recipe/", views.DeleteRecipe.as_view(), name="delete_recipe"),
    path("recipes/add_recipe_requirement/", views.AddRecipeRequirement.as_view(), name="add_recipe_req"),
    path("recipes/<pk>/update_recipe_requirement/", views.UpdateRecipeRequirement.as_view(), name="update_recipe_req"),
    path("recipes/<pk>/delete_recipe_requirement/", views.DeleteRecipeRequirement.as_view(), name="delete_recipe_req"),
]