#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:54:07 2017

@author: Zakery and Richard

"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, KMeans, SpectralClustering

class HWCluster(object):
    
    def __init__(self):
    
        self.data_columns = ['Column1', 'Column2']
        self.data_dir = './../dataset/'
        self.filenames = ['Clustering1', 'Clustering2', 'Clustering3', 'Clustering4', 'Clustering5']
    
    def load_dataset(self, filename):
        
        file = os.path.join( self.data_dir , filename )
        dataset = pd.read_table(file, delimiter='\t')
        
        return dataset[self.data_columns]
        
    def plot_dataset(self, dataset, title, labels=None):
        
        if labels is None:
            plt.scatter( dataset['Column1'], dataset['Column2'] )
        else:
            plt.scatter( dataset['Column1'], dataset['Column2'], c=labels )
        plt.title(title)    
        plt.show()
        
    def explore_dataset(self):
        
        for filename in self.filenames:
            
            dataset = self.load_dataset( filename + ".txt" )
            self.plot_dataset( dataset, filename)
            
    def dbscan_clustering(self):
        
        for filename in self.filenames:
            
            dataset = self.load_dataset( filename + ".txt" )
            db = DBSCAN(eps=2.5, n_jobs=-1).fit(dataset)

            self.plot_dataset( dataset, 'DBScan Clustering', db.labels_)
                
    def kMeans_clustering(self, clusters):
        
        for filename in self.filenames:
            
            dataset = self.load_dataset( filename + ".txt" )
            kmeans_model = KMeans(n_clusters=clusters).fit(dataset)
            self.plot_dataset( dataset, 'KMeans Clustering', kmeans_model.labels_)
            
    def spectral_clustering(self, clusters):
        
        for filename in self.filenames:
            
            dataset = self.load_dataset( filename + ".txt" )
            spectral_model = SpectralClustering(n_clusters=clusters, n_jobs=-1, eigen_solver='arpack',
        affinity="nearest_neighbors").fit(dataset)
            self.plot_dataset( dataset, 'Spectral Clustering', spectral_model.labels_ )
            
        

if __name__ == '__main__':
    
    hw_cluster = HWCluster()
    
    #hw_cluster.explore_dataset()
    #hw_cluster.kMeans_clustering(4)
    #hw_cluster.dbscan_clustering()
    hw_cluster.spectral_clustering(2)