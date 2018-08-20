import pickle
import gensim
import sys
import pandas as pd
import numpy as np


def get_top_n(n,word_vec):
    df_name = './data/pickled_df'
    with open(df_name, 'rb') as f:
        df = pickle.load(f)
    #df = pd.read_json('./data/full_format_recipes.json')
    print(df.columns)
    def calculate_difference(recipe_vec):
        diff = word_vec - recipe_vec
        return np.sum(diff**2)
    df['diff'] = df['vec'].map(calculate_difference)
    result = df.sort_values(by='diff').head(n)
    return result


def run_pickle_model(modelname, word):
    with open(modelname, 'rb') as f:
        word2vec_pickle_model = pickle.load(f)
    this_word_vector = word2vec_pickle_model.wv[word]
    result = get_top_n(10,this_word_vector)
    print(result)
    return result


if __name__ == "__main__":
    modelname = "./word2vec_model"
    word = input("Please enter an ingredient: ")
    run_pickle_model(modelname, word)
