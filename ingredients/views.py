from .forms import IngredientForm
from django.views.generic.edit import FormView


class IngredientView(FormView):
    template_name = 'ingredients/ingredient_input.html'
    form_class = IngredientForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        ingredient = form.cleaned_data.get('ingredient')
        modelname = "./word2vec_model"
        form.send_ingredient(modelname, ingredient)
        return super().form_valid(form)
