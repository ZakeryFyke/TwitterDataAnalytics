#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:31:00 2017

@author: matrich
"""

import os
import pandas as pd

class TopicDiscoverer(object):
    
    def __init__(self):
        
        self.data_dir = './../datasets/'
        
    
    def load_datasets(self):
        
        files = [f for f in os.listdir(self.data_dir) if 'tweets.csv' in f]
        
        for f in files:
            
            file = os.path.join( self.data_dir , f )
            
            df = pd.read_csv(file, names=['tweet'])
            
        
            print( df.head(100) )
            
            break
        
        '''
        
        dataset = pd.read_table(file, delimiter='\t')
        
        return dataset[self.data_columns]
        '''
        

td = TopicDiscoverer()
td.load_datasets()