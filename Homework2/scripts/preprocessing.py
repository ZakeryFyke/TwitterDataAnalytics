#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:42:48 2017

@author: Zakery and Richard
"""

import nltk
import pandas as pd

def get_stop_words_list():
    df = pd.read_csv('./../resources/stopWords.txt', names=['stopWord'])
    
    return set( df['stopWord'] )

def remove_stop_words(tweet, stopWords):
    
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]
    return " ".join(filtered_words)

def filter_data():
    
    df = pd.read_csv('./../Dataset/harvey_tweets.tweets.csv')   
    df = df[df['is_retweet'] == True]
    
    tweets = df[['text']]

    print( tweets.head() )
    
    tokens = nltk.wordpunct_tokenize( tweets.iloc[4]['text'] )
    
    print(tokens)
    
    text = nltk.Text(tokens)
    
    words = [w.lower() for w in text if w.isalpha()]
    
    print(words)
    
    
filter_data()

#print( get_stop_words() )


'''

    tokens = nltk.wordpunct_tokenize(raw)
    
    type(tokens)
    
    text = nltk.Text(tokens)
    
    type(text)  
    
    words = [w.lower() for w in text if w.isalpha()]

'''