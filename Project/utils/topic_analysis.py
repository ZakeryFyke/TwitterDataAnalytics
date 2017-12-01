#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:13:40 2017

@author: matrich
"""

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import os
import pandas as pd
import gensim
from gensim import corpora, models
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class TopicAnalysis(object):
    
    def __init__(self):
        words = set(line.strip().lower() for line in open('stopwords.txt'))
        self.stop = set(stopwords.words('english')).union(words)
        self.exclude = set(string.punctuation)
        self.lemma = WordNetLemmatizer()
    
        self.data_columns = ['tweet']
        self.data_dir = './../senatordatasets/tweets/'
        
    def load_dataset(self, party):
        
        filename = "All" + party + "Tweets.csv"

        file = os.path.join( self.data_dir, filename  )
        dataset = pd.read_csv(file, delimiter='\t', names=['tweet'])
        
        return dataset[self.data_columns]
    
    def clean_tweet(self, doc):
        
        tweet = str( doc['tweet'] )
        
        punc_free = ''.join(ch for ch in tweet if ch not in self.exclude)
        stop_free = " ".join( [i for i in punc_free.lower().split() if i not in self.stop] )
        normalized = " ".join(self.lemma.lemmatize(word) for word in stop_free.split())
        
        return normalized
    
    def train_model(self, party, num_topics=7):
        
        tweet_dataset = self.load_dataset(party)
        
        cleaned_tweets = [self.clean_tweet(tweet).split() for index, tweet in tweet_dataset.iterrows()]
        
        # Creating the term dictionary of our courpus, where every unique term is assigned an index. 
        dictionary = corpora.Dictionary(cleaned_tweets)
        
        # TF for the documents
        tfidf = models.TfidfModel(dictionary=dictionary)
        
        # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in cleaned_tweets]
        
        #print( doc_term_matrix[2] )
        corpus_tfidf = tfidf[doc_term_matrix]
        
        # Creating the object for LDA model using gensim library
        Lda = gensim.models.ldamodel.LdaModel
        
        # Running and Training LDA model on the document term matrix.
        ldamodel = Lda(corpus_tfidf, num_topics=num_topics, id2word = dictionary, passes=50)
        
        return ldamodel
    
ta = TopicAnalysis()
        
ec_model = ta.train_model("Democrats", 7)
print( ec_model.print_topics(7, 30) )
