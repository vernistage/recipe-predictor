from django.shortcuts import render, redirect

from .forms import IngredientForm


def ingredient_input(request):
    context = {}
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.cleaned_data['ingredient']
            context['form'] = IngredientForm()
            context['recipes'] = form.send_ingredient("./word2vec_model", ingredient)
            return render(request, 'ingredients/ingredient_input.html', context)
    else:
        form = IngredientForm()
        context['form'] = form
        return render(request, 'ingredients/ingredient_input.html', context)
