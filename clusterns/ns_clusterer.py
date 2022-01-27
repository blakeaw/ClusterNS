import warnings
import numpy as np
import multiprocessing as mp

class NSClusterer(object):

    def __init__(self, max_clusters=5, pop_size=100):
        self.max_clusters = max_clusters
        self.pop_size = pop_size
        self.labels = None
        self.n_samples = None
        self.n_features = None
        return

    def fit(self, X, nprocs=1):
        self.n_samples = X.shape[0]
        self.n_features = X.shape[1]
            
