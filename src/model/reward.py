# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:42:56 2017

@author: Eleden
"""

# -*- coding: utf-8 -*-

from random import randrange

class Reward:

    def __init__(self):   

        self._data = dict()
        
    # index must be a tuple (state,action)
    def __getitem__(self,index):
       
        try:
            return self._data[index]
        
        except KeyError:
            self._data[index] = 0
            return self._data[index]
            
    
    def __setitem__(self,index,value):

        self._data[index] = value

    def maxActionValueOn(self,s):
        
        # key[0] : State
        # key[1] : Action
        # l = list of tuple(action,value) on the state s
        l = [ (key[1],value) for key,value in self._data.items() if key[0] == s]
        t = max(l,key = lambda x : x[1])     
        return t
    
    def bestActionOn(self,s):
        
        return self.maxActionValueOn(s)[0]
    
    def maxValueOn(self,s):
        
        return self.maxActionValueOn(s)[1]
    
    def __repr__(self):
        
        return self._data.__repr__()
    
    def __str__(self):
        
        return self._data.__str__()
    
    def __values__(self):
        
        return self.__dict__.values()