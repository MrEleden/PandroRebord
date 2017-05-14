# -*- coding: utf-8 -*-
import scipy.io
from random import randrange


class Menu:
    
    def __init__(self,config):
        self._menu = None
        self._decision = None
        self._data = []
        self._target = None
        
        for relevance in config.relevances:
           temp = scipy.io.loadmat(relevance['dbname'])
           temp = temp[relevance['name']]
           self._data.append(temp)
        
        self.size = len(self._data[0][0])
        self._fill = []
        for i in range(self.size + 2):
            self._fill[i]=False
  
            
    def newCycle(self):
        self._menu = randrange(0,len(self._data[0]))
        
    def execute(self,action):
        if action.type == action.SELECT:
            self._decision = 1
        elif action.type == action.fixate:
            self._decision = 0
        else:
            self._decision = -1
        relevance = []
        for l in self._data:
            relevance.append(l[self._menu][action.item])
        self._fill[action.item + 2] = True;
            
        return action.item,relevance
    
    def reward(self,dist):
        
        time = 437 + 2.7 * dist
        score = -10000
        
        for b in self._fill:
            if not b:
                score = 10000
                break
        
        if self._decision == 1:
            value = score
        elif self._decision == 0:
            value = -score
        else:
            value = -3*score
            
        return value - time
    
    def getvalue(self,rel,menu,item):
        return self._data[rel][menu][item]