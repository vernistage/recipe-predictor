from django.shortcuts import render, redirect

from .forms import IngredientForm


def ingredient_input(request):
    context = {}
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.cleaned_data['ingredient']
            context['form'] = IngredientForm()
            recipes = form.send_ingredient("data/word2vec_model", ingredient)
            context['recipes'] = recipes[:3]
            context['recommended_recipes'] = recipes[3:9]
            context['ingredient'] = ingredient
            return render(request, 'ingredients/ingredient_input.html', context)
    else:
        form = IngredientForm()
        context['form'] = form
        return render(request, 'ingredients/ingredient_input.html', context)

# Index(['calories', 'categories', 'date', 'desc', 'directions', 'fat',
#        'ingredients', 'protein', 'rating', 'sodium', 'title',
#        'gensim_directions', 'gensim_directions_doc', 'vec', 'diff'],
#       dtype='object')
