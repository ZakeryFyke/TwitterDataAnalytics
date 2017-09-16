# Note: Due to time constraints on how long tweets are maintained, we are using a pregathered dataset instead of the
# results of our webcrawling for this homework

from math import *
import pandas as pd
import random
import numpy as np


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


# Returns an N x N array
def create_array(n):
    return np.zeros(shape=(n,n))


#random_row_selector(10, "C:/Users/Zakery/Documents/GitHub/TwitterDataAnalytics/Datasets/Hurricane_Harvey.csv")
