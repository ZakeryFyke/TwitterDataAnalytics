#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:54:07 2017

@author: Zakery and Richard

"""

import os
import pandas as pd
import matplotlib.pyplot as plt

class HWCluster(object):
    
    def __init__(self):
    
        self.data_dir = './../dataset/'
        self.filenames = ['Clustering1', 'Clustering2', 'Clustering3', 'Clustering4', 'Clustering5']
    
    def load_dataset(self, filename):
        
        file = os.path.join( self.data_dir , filename )
        dataset = pd.read_table(file, delimiter='\t')
        
        return dataset
        
    def plot_dataset(self, dataset):
        
        plt.scatter( dataset['Column1'], dataset['Column2'] )
        plt.show()
        
    def explore_dataset(self):
        
        for filename in self.filenames:
            
            dataset = self.load_dataset( filename + ".txt" )
            self.plot_dataset( dataset )
        

if __name__ == '__main__':
    
    hw_cluster = HWCluster()
    
    hw_cluster.explore_dataset()
