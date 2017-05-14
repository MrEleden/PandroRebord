# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:29:27 2017

@author: Eleden
"""

# -*- coding: utf-8 -*-

from random import randrange
import numpy as np
class Proba:

    def __init__(self,ne):   
        self.ne = ne
        self._data = dict()
        
    # index must be a tuple (state,action,state)
    def __getitem__(self,index):
       
        try:
            return self._data[index]
        
        except KeyError:
            proba = np.random.dirichlet(np.ones(self.ne),size=1)
          
            s1,a,s2 = index
            for i in range(self.ne):
                self._data[(s1,a,i)] = proba[0][i]
               
            return self._data[index]
            
    
    def __setitem__(self,index,value):

        self._data[index] = value

    def __repr__(self):
        
        return self._data.__repr__()
    
    def __str__(self):
        
        return self._data.__str__()
    
    def __values__(self):
        
        return self.__dict__.values()