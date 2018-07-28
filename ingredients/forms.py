import pickle
import gensim
import sys

from django import forms


class IngredientForm(forms.Form):
    ingredient = forms.CharField(label='Input an ingredient', max_length=100)

    def send_ingredient(self, modelname, ingredient):
        with open(modelname, 'rb') as f:
            word2vec_pickle_model = pickle.load(f)
        result = word2vec_pickle_model.wv.most_similar(positive=ingredient)
        print(result)
        return result
