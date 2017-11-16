# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import re
import lda.datasets
from sklearn.feature_extraction.text import CountVectorizer

class HWLDA(object):
    
    def __init__(self):

        self.data_columns = ['tweet']
        self.data_dir = './../project/senatordatasets'
        self.filenames = ['SenWarrenTweets', 'marcorubiotweets', 'CoryBookertweets', 'RandPaultweets', 'SenJohnMcCaintweets'
                          'SenTedCruztweets', 'KamalaHarristweets', 'timkainetweets', 'SenSanderstweets', 'SenSchumertweets']

    def load_dataset(self, filename):

        file = os.path.join( self.data_dir , filename + ".csv" )
        dataset = pd.read_csv(file, delimiter='\t', names=['tweet'])
        
        return dataset[self.data_columns]



if __name__ == '__main__':

    hw_lda = HWLDA()

    token_dict = {}

    tweets = hw_lda.load_dataset('SenWarrenTweets')

    # Number of topics
    num = 10

    # Build the DTM
    tf = CountVectorizer(stop_words='english')

    # Place tweets into dictionary
    for i in range(len(tweets)):

        # Have to replace unicode characters so they don't appear in the topics
        token_dict[i] = tweets['tweet'][i].replace("â€™", "'").replace("&amp;", "and")


    # Fit the DTM
    tfs = tf.fit_transform(token_dict.values())

    # Get vocab of DTM
    vocab = tf.get_feature_names()

    model = lda.LDA(n_topics=num, n_iter=5000, random_state=1)

    model.fit(tfs)

    topic_word = model.topic_word_

    n = 30
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n + 1):-1]
        print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

    # n_top_words = 5
    #
    # for i, topic_dist in enumerate(topic_word):
    #     topic_words = np.array(token_dict)[np.argsort(topic_dist)][:-n_top_words:-1]
    #
    # print('Topic {}: {}'.format(i, ' '.join(topic_words)))