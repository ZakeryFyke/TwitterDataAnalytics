
"""
Created on Mon Sep 25 15:42:48 2017

@author: Zakery and Richard
"""


import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer


class HarveyRescueKNN(object):
    
    def __init__(self, train_size=0.6):
        
        self.train_size = train_size
        
        self.load_dataset()

    def get_stop_words_list(self):
        
        df = pd.read_csv('./../resources/stopWords.txt', names=['stopWord'])
        return set( df['stopWord'] )
    
    def load_dataset(self):
        
        tweet_df = pd.read_csv('./../Dataset/harvey_tweets.sample.csv', names=['tweet', 'category'])
        
        tweets = np.asarray(tweet_df['tweet'])
        categories = np.asarray( tweet_df['category'] )
        
        self.X_train, self.X_test, self.y_train, self.y_true = train_test_split(tweets, categories, train_size=self.train_size, random_state=4332)

    def classify(self, k=2, p=2):
        
        stop_words_list = self.get_stop_words_list()
        vectorizer = CountVectorizer(stop_words=stop_words_list )
        
        train_features = vectorizer.fit_transform(self.X_train)
        
        test_features = vectorizer.transform(self.X_test)
        test_features = test_features.toarray()
        
        rescue_detector = KNeighborsClassifier(n_neighbors=k, p=p, n_jobs=-1)
        rescue_detector.fit(train_features, self.y_train)
        
        y_pred = rescue_detector.predict(test_features)
        
        recallScore = recall_score( self.y_true, y_pred, labels=['Non-Rescue', 'Rescue'], pos_label='Rescue' )
        precisionScore = precision_score( self.y_true, y_pred, labels=['Non-Rescue', 'Rescue'], pos_label='Rescue' )
        f1Score = f1_score( self.y_true, y_pred, labels=['Non-Rescue', 'Rescue'], pos_label='Rescue' )
        
        return recallScore, precisionScore, f1Score
        
        
        
def main():
    
    for k in range(1, 20):
        
        clf = HarveyRescueKNN()
        
        results = clf.classify(k=k, p=2)
        print(k, results[0], results[1], results[2])
    
    print()


if __name__ == '__main__':
    main()
