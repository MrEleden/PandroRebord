# -*- coding: utf-8 -*-

import random as r

class Actions:
    
    EXIT = -1
    FIXATE = 0
    SELECT = -2
    
    def __init__(self,menuSize):
        
        self._menuSize = menuSize
    
    def __repr__(self):
        
        if(self.action == Actions.EXIT):
            return "EXIT"
        elif(self.action == Actions.SELECT):
            return "SELECT"
        else:
            return "FIXATE-" + str(self.item)
    
    def __str__(self):
        
        return self.__repr__()
    
    def random(self):
        
        n = r.randrange(1,self._menuSize,1)
            
        self.type = Actions.FIXATE
        self.item = n
        
        return self
    
    
    