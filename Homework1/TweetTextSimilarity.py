# Note: Due to time constraints on how long tweets are maintained, we are using a pregathered dataset instead of the
# results of our webcrawling for this homework
import pandas as pd
import random
import numpy as np

from SimilarityFunctions import *

# Takes N random samples from the passed csv
def random_row_selector(n, csv_file_path):
    rows = get_number_of_csv_rows(csv_file_path)

    skip = sorted(random.sample(range(rows), rows-n))
    df = pd.read_csv(csv_file_path, skiprows = skip, encoding="mbcs")

    return df


# Returns the number of rows in a csv
def get_number_of_csv_rows(path):
    with open(path) as csvfile:
        row_count = sum(1 for row in csvfile)
    return row_count


# Returns an N x N matrix
def create_matrix(n):
    return np.zeros(shape=(n,n))


def create_levenshtein_distance_matrix(series):
    matrix = create_matrix(len(series))

    for i in range(0, len(series)):
        tweet1 = series[i]
        for j in range(0, len(series)):
            tweet2 = series[j]
            matrix[i,j] = levenshtein(tweet1, tweet2)

    return matrix

def create_matching_ratio_matrix(series):
    matrix = create_matrix(len(series))

    for i in range(0, len(series)):
        tweet1 = series[i]
        for j in range(0, len(series)):
            tweet2 = series[j]
            matrix[i,j] = matching_words_ratio(tweet1, tweet2)

    return matrix

def create_cosine_distance_matrix(series):
    matrix = create_matrix(len(series))

    for i in range(0, len(series)):
        tweet1 = series[i]
        for j in range(0, len(series)):
            tweet2 = series[j]
            matrix[i,j] = cosine_similarity(tweet1, tweet2)

    return matrix

df = random_row_selector(10, "C:/Users/Zakery/Documents/GitHub/TwitterDataAnalytics/Datasets/Hurricane_Harvey.csv")
df.columns = ["count", "id", "likes", "replies", "retweets", "time", "tweet"]
df = df.iloc[:, 6]


