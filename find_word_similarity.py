from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import sys

def get_tfidf_matrix(dataset):
    '''
        This function makes a tfidf matrix from the dataset provided

        :param dataset: A Pandas Series Frame dataset file
    '''
    #Define the TFIDF vectorizer that will be used to process the data
    tfidf_vectorizer = TfidfVectorizer()
    #Apply this vectorizer to the full dataset to create normalized vectors
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset)
    return tfidf_matrix

def get_closest_neighs(word, tfidf_matrix):
    '''
        Function to find the similar terms using tfidf matrix

        :param word: Word of which similar words are to be found out
        :param tfidf_matrix: TF-IDF matrix returned by get_tfidf_matrix()
    '''
    nbrs = NearestNeighbors(n_neighbors=10).fit(tfidf_matrix)
    row = dataset.index.get_loc(word)
    distances, indices = nbrs.kneighbors(tfidf_matrix.getrow(row))
    names_similar = pd.Series(indices.flatten()).map(dataset.reset_index()['tag'])
    result = pd.DataFrame({'distance':distances.flatten(), 'name':names_similar})
    return result

if __name__ == '__main__':
    dataset = pd.read_csv('dataset.csv', index_col='tag')['context']
    tfidf_matrix = get_tfidf_matrix(dataset)
    if len(sys.argv) > 1:
        print(get_closest_neighs(sys.argv[1].lower(), tfidf_matrix))
    else:
        print('Please provide a word to search for similar words!')
