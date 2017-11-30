from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
import os

class SimpleGroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


def normalize_dict(D):
    maximum = max(D.values())
    for k in D:
         D[k] = D[k] / maximum

    return D

os.chdir('..')
directoryPath = os.getcwd() + '\EchoChambersReport'

def get_color_to_words(D):
    color_to_words = {}
    color_options = ['placeholder', '#a6cee3', '#1f78b4', '#b2df8a', '#000000', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00',
                     '#cab2d6', '#6a3d9a', '#fcf811', '#b15928']

    for topic in D.keys():

        color = color_options[topic]

        color_to_words[color] = (D[topic]).keys()

    return color_to_words


def compare_topic_words(file1, file2):

    with open(directoryPath + '/' + file1) as myfile:
        data1 = myfile.read().replace('\n', '')

    with open(directoryPath + '/' + file2) as myfile:
        data2 = myfile.read().replace('\n', '')

    L1 = get_terms_with_probability(data1)
    L2 = get_terms_with_probability(data2)

    topics1 = L1.keys()
    topics2 = L2.keys()

    shared_topics = list(set(topics1).intersection(topics2))
    print(shared_topics)

    print(str(len(topics1)))
    print(str(len(topics2)))
    print(str(len(shared_topics)))

def get_terms_with_probability(data):
    sublists = data.split(',')

    L = {}
    for i in range(1, len(sublists), 2):
        items = (sublists[i][3:].split('+'))
        for item in items:
            partial = item.split('*')

            prob = float(partial[0].strip())
            term = partial[1].strip().replace('"', '')

            # Remove special symbol terms and terms like "u" or "w"
            if ')' not in term and '\\' not in term and len(term) >= 3:

                if(term not in L.keys()):
                    L[term] = prob
                elif(L[term] < prob):
                    L[term] = prob

    return L

def plot_topic_word_cloud(file):
    with open(directoryPath + '/' + file) as myfile:
        data = myfile.read().replace('\n', '')

    sublists = data.split(',')

    bigD = {}
    littleD = {}
    count = 1
    for i in range(1, len(sublists), 2):
        # print(sublists[i])

        items = (sublists[i][3:].split('+'))

        L = {}

        for item in items:
            partial = item.split('*')

            prob = float(partial[0].strip())
            term = partial[1].strip().replace('"', '')

            # Remove special symbol terms and terms like "u" or "w"
            if ')' not in term and '\\' not in term and len(term) >= 3:

                if(term not in littleD.keys()):
                    L[term] = prob
                    littleD[term] = prob
                elif(littleD[term] < prob):
                    L[term] = prob
                    littleD[term] = prob

        bigD[count] = normalize_dict(L)

        L = {}
        count += 1

    littleD = normalize_dict(littleD)

    print bigD
    print littleD

    wordcloud = WordCloud(background_color='white', width=2000, height=1500).generate_from_frequencies(littleD)

    color_to_words = get_color_to_words(bigD)

    grouped_color_func = SimpleGroupedColorFunc(color_to_words, 'grey')

    wordcloud.recolor(color_func=grouped_color_func)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# plot_topic_word_cloud('Democrats_Topic_Probability.txt')
compare_topic_words('Democrats_Topic_Probability.txt', 'Republicans_Topic_Probability.txt')