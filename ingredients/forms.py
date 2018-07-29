import pickle
import gensim
import numpy as np
import pandas as pd
import sys

from django import forms


class IngredientForm(forms.Form):
    ingredient = forms.CharField(label='Input an ingredient', max_length=100)

    def get_top_n(self, n, word_vec):
        df_name = './data/pickled_df'
        with open(df_name, 'rb') as f:
            df = pickle.load(f)
        # print(df.columns)

        def calculate_difference(recipe_vec):
            diff = word_vec - recipe_vec
            return np.sum(diff**2)
        df['diff'] = df['vec'].map(calculate_difference)
        result = df.sort_values(by='diff').head(n)
        return result

    def send_ingredient(self, modelname, ingredient):
        with open(modelname, 'rb') as f:
            word2vec_pickle_model = pickle.load(f)
        this_word_vector = word2vec_pickle_model.wv[ingredient]
        similar_words = word2vec_pickle_model.wv.most_similar(ingredient)
        similar_word = similar_words[0][0]
        similar_word_vec = word2vec_pickle_model.wv[similar_word]
        result1 = self.get_top_n(3, this_word_vector)
        result2 = self.get_top_n(6, similar_word_vec)
        frame = [result1, result2]
        new_frame = pd.concat(frame, axis=0)[['title', 'ingredients', 'directions']]
        result = new_frame.to_dict('records')
        print(result)
        return result
