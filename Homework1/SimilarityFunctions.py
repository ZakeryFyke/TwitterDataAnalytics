import numpy as np
import math
import re
from collections import Counter
WORD = re.compile(r'\w+')


# returns the Levenshtein Distance between two strings
def levenshtein(source, target):

    if len(source) < len(target):
        return levenshtein(target, source)

    if len(target) == 0:
        return len(source)

    source = np.array(tuple(source))
    target = np.array(tuple(target))

    previous_row = np.arange(target.size + 1)
    for s in source:

        current_row = previous_row + 1

        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]


# Returns the ratio of words in S2 that also appear in S1.
def matching_words_ratio(s1, s2):
    s1_list = s1.lower().split()
    s2_list = s2.lower().split()
    return len((set(s1_list).intersection(s2_list)))/len(s2_list)


# Gets the cosine value between two vectors
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


# Converts a sentence to a vector of strings which can be used to calculate cosine values
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def cosine_similarity(s1, s2):
    s1_vec = text_to_vector(s1)
    s2_vec = text_to_vector(s2)

    return get_cosine(s1_vec, s2_vec)