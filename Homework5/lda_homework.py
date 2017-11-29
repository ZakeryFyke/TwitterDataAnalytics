# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import lda.datasets
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import collections
import csv

class HWLDA(object):
    
    def __init__(self):

        self.data_columns = ['tweet']
        self.data_dir = './../project/senatordatasets'
        self.filenames = ['SenWarrenTweets', 'marcorubiotweets', 'CoryBookertweets', 'RandPaultweets', 'SenJohnMcCaintweets'
                          'SenTedCruztweets', 'KamalaHarristweets', 'timkainetweets', 'SenSanderstweets', 'SenSchumertweets']

    def load_dataset(self, party, filename):

        file = os.path.join( self.data_dir, party + '/' + filename + ".csv" )
        dataset = pd.read_csv(file, delimiter='\t', names=['tweet'])
        
        return dataset[self.data_columns]


    def compare_number_of_topics(self, party, dataset, max, iter):
        topic_likelihood_dict = {}

        tf = CountVectorizer(stop_words='english')

        tweets = hw_lda.load_dataset(party, dataset)

        token_dict = {}
        for i in range(len(tweets)):
            # Have to replace unicode characters so they don't appear in the topics
            token_dict[i] = str(tweets['tweet'][i]).replace("â€™", "'").replace("&amp;", "and")

        tfs = tf.fit_transform(token_dict.values())

        # Get vocab of DTM
        vocab = tf.get_feature_names()

        for topic_count in range(1, max):
            model = lda.LDA(n_topics=topic_count, n_iter=iter, random_state=1)

            model.fit(tfs)

            print("Likelihood for " + str(topic_count) + " topics is " + str(model.loglikelihood()))

            topic_likelihood_dict[topic_count] = model.loglikelihood()

        od = collections.OrderedDict(sorted(topic_likelihood_dict.items()))
        return od

    def run_lda(self, numberoftopics, party, datasets):

        #tf = CountVectorizer(stop_words='english')
        words = set(line.strip().lower() for line in open('stopwords.txt'))

        tf = CountVectorizer(stop_words=words)

        for dataset in datasets:
            print('###################################')
            tweets = hw_lda.load_dataset(party, dataset)

            token_dict = dict()
            for i in range(len(tweets)):
                # Have to replace unicode characters so they don't appear in the topics
                token_dict[i] = str(tweets['tweet'][i]).replace("â€™", "'").replace("&amp;", "and")

            # Fit the DTM using our dictionary
            tfs = tf.fit_transform(token_dict.values())

            # Get vocab of DTM
            vocab = tf.get_feature_names()

            model = lda.LDA(n_topics=numberoftopics, n_iter=2000, random_state=1)

            model.fit(tfs)

            topic_word = model.topic_word_

            print('Topics for: ' + dataset)
            n = 10
            for i, topic_dist in enumerate(topic_word):
                topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n + 1):-1]
                print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

            print('###################################')



if __name__ == '__main__':

    hw_lda = HWLDA()

    # TODO: Grab these programmatically
    # csvs = ['marcorubiotweets', 'SenWarrenTweets', 'SenSchumerTweets', 'SenSanderstweets','timkainetweets',
    #             'SenJohnMcCaintweets', 'RandPaultweets','KamalaHarristweets','CoryBookerTweets', 'SenTedCruztweets']

    topic_dict = hw_lda.compare_number_of_topics('Republicans', 'AllRepublicansTweets', 100, 2000)
    topics = topic_dict.keys()
    likelihoods = topic_dict.values()
    print("Max likelihood for " + 'Republicans' + " was " + str(max(topic_dict, key=topic_dict.get)))

    L = topic_dict.items()
    print(L)

    with open('RepublicanLDA.csv', 'wb') as out:
        csv_out = csv.writer(out)
        for row in L:
            csv_out.writerow(row)

    topic_dict = hw_lda.compare_number_of_topics('Democrats', 'AllDemocratsTweets', 100, 2000)
    topics = topic_dict.keys()
    likelihoods = topic_dict.values()
    print("Max likelihood for " + 'Democrats' + " was " + str(max(topic_dict, key=topic_dict.get)))

    L = topic_dict.items()
    print(L)

    with open('DemocratLDA.csv', 'wb') as out:
        csv_out = csv.writer(out)
        for row in L:
            csv_out.writerow(row)

    # plt.plot(topics, likelihoods)
    # plt.title('Republicans')
    # plt.ylabel('Log Likelihood')
    # plt.xlabel('Number of topics')
    # plt.show()


    # hw_lda.run_lda(10,'Democrats', ['AllDemocratsTweets'])
    # hw_lda.run_lda(10, 'Republicans', ['AllRepublicansTweets'])
    # for dataset in csvs:
    #     topic_dict = hw_lda.compare_number_of_topics(dataset, 100)
    #     topics = topic_dict.keys()
    #     likelihoods = topic_dict.values()
    #
        # print("Max likelihood for " + dataset + " was " + str(max(topic_dict, key=topic_dict.get)))
        #
        # plt.plot(topics, likelihoods)
        # plt.title(dataset)
        # plt.ylabel('Log Likelihood')
        # plt.xlabel('Number of topics')
        # plt.show()