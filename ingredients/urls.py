from django.urls import path
from . import views

urlpatterns = [
    path('ingredient/', views.ingredient_input, name='ingredient-input'),
]
