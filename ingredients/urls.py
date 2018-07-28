from django.urls import path
from . import views

urlpatterns = [
    path('ingredient/', views.IngredientView.as_view(), name='ingredient-input'),
    # path('recipes/', views.ingredient, name='recipes-list'),
]
