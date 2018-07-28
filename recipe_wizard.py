import pickle
import gensim
import sys


def run_pickle_model(modelname, word):
    with open(modelname, 'rb') as f:
        word2vec_pickle_model = pickle.load(f)
    result = word2vec_pickle_model.wv.most_similar(positive=word)
    print(result)
    return result


if __name__ == "__main__":
    modelname = "./word2vec_model"
    word = input("Please enter an ingredient: ")
    run_pickle_model(modelname, word)
