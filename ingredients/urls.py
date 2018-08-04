from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient_input, name='ingredient-input'),
]
