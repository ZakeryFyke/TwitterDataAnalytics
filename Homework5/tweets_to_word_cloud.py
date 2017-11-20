import csv
from wordcloud import WordCloud, STOPWORDS
import os
import matplotlib.pyplot as plt


def create_word_cloud(filename):

    filepath = os.path.join('./../project/senatordatasets', filename + ".csv")
    list = []
    with open(filepath, 'rb') as f:
        reader = csv.reader(f)
        list = '\t'.join([i[0] for i in reader])

    stopwords = set(STOPWORDS)
    stopwords.add('amp')
    stopwords.add('will')
    stopwords.add('must')
    stopwords.add('want')
    stopwords.add('today')
    # stopwords.add('SenTedCruz')
    # stopwords.add('SenSanders')

    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords).generate(list)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(filename + " Word Cloud")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(list)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(filename + " Word Cloud")
    plt.show()

csvs = ['SenTedCruztweets', 'SenSanderstweets']

for c in csvs:

    create_word_cloud(c)