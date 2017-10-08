
"""
Created on Mon Sep 25 15:42:48 2017

@author: Zakery and Richard
"""


import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer


class HarveyRescue(object):
    
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

    def extract_features(self):
        
        stop_words_list = self.get_stop_words_list()
        vectorizer = CountVectorizer(stop_words=stop_words_list, max_df=0.1 )
        
        train_features = vectorizer.fit_transform(self.X_train)
        
        test_features = vectorizer.transform(self.X_test)
        test_features = test_features.toarray()
        
        return train_features, test_features
    
    def compute_fScore(self, y_true, y_pred):
        
        recallScore = recall_score( self.y_true, y_pred, labels=['Non-Rescue', 'Rescue'], pos_label='Rescue' )
        precisionScore = precision_score( self.y_true, y_pred, labels=['Non-Rescue', 'Rescue'], pos_label='Rescue' )
        f1Score = f1_score( self.y_true, y_pred, labels=['Non-Rescue', 'Rescue'], pos_label='Rescue' )
        
        return recallScore, precisionScore, f1Score

    
    def classify_with_kNN(self, k=2, p=2):
        
        train_features, test_features = self.extract_features()
        
        rescue_detector = KNeighborsClassifier(n_neighbors=k, p=p, n_jobs=-1)
        rescue_detector.fit(train_features, self.y_train)
        
        y_pred = rescue_detector.predict(test_features)
        
        return self.compute_fScore(self.y_true, y_pred)

    def classify_with_SVM(self, c = 1000, kernel = 'rbf'):
        
        train_features, test_features = self.extract_features()

        svm_clf = SVC(C = c, kernel=kernel)
        svm_clf.fit(train_features, self.y_train)
        
        y_pred = svm_clf.predict(test_features)
        
        return self.compute_fScore(self.y_true, y_pred)
        
def kNN_classifier():

    for k in range(1, 21):
        
        clf = HarveyRescue()
        
        results = clf.classify_with_kNN(k=k, p=2)
        
        print(k, results[0], results[1], results[2])
        print()
        
def svm_classifier():
    
    clf = HarveyRescue()
    for kernel in ('linear', 'poly', 'rbf', 'sigmoid'):
        print("Kernel Type: " + kernel)
        for c in xrange(100, 5000, 100):
            results = clf.classify_with_SVM(c, kernel)
            print(c, results[0], results[1], results[2])
            print()
        print("========")


if __name__ == '__main__':
    #print('kNN Classification')
    #kNN_classifier()
    print('SVM Classification')
    svm_classifier()
