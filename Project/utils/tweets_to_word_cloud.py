import csv
from wordcloud import WordCloud, STOPWORDS
import os
import matplotlib.pyplot as plt
from scipy.misc import imread

os.chdir('..')

directoryPath = os.getcwd()+ '\SenatorDataSets'

def create_word_cloud(party, filename, title):

    twitter_mask = imread(os.getcwd() + '/utils/twitter_mask.png', flatten=True)

    filepath = directoryPath + '/' + party + '/' + filename + '.csv'

    with open(os.getcwd() + '/utils/stopwords.txt') as f:
        extrastops = f.readlines()
        extrastops = [x.strip() for x in extrastops]

    list = []
    with open(filepath, 'rb') as f:
        reader = csv.reader(f)
        list = '\t'.join([i[0] for i in reader])

    stopwords = set(STOPWORDS)
    stopwords = stopwords.union(extrastops)

    print(len(list))

    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords,
                          mask=twitter_mask,
                          background_color='white',
                          max_words=1000).generate(list)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title(title)

    plt.show()

create_word_cloud('Republicans', 'AllRepublicansTweets', 'Republican Tweet Word Cloud')
create_word_cloud('Democrats', 'AllDemocratsTweets', 'Democrat Tweet Word Cloud')