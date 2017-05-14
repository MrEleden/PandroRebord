# -*- coding: utf-8 -*-

class States:
    
    def __init__(self,menusize,names):
        self._menuSize = menusize
        self._names = names
        self._finalState = False
        
    def init(self):
		
        self._relevances = dict()
        for name in self._names:
            self._relevances[name] = [None for i in range(0,self._menuSize)]
		
        self._fixate = None
        self._state = "S0"
        
    def currentState(self):
        return self._state
	
    def _setState(self):
        s = "S"	
		
        for relevance in self._relevances.values():
            for value in relevance:
                s += self._valueOf(value)
        s += str(self._fixate)
	
        self._state = s
			
    def updateState(self,updates):
        index = updates[0]
        if(index == -1 or index == -2):
            self._finalState = True
        else:
            print(index)
            select = False
            for update in updates[1]:
                self._relevances[update["vector_name"]][index] = update["relevance"]
                
                
        if(select):
            self._fixate = self._menuSize +1
        else:
            self._fixate = index
        self._setState()
    
    def finalState(self):
        return self._finalState            
		
    def _valueOf(self,i):
		
        if(i == None):
            return  0
        elif(i == 0):
            return 1
        elif(i == 0.3):
            return 2
        elif(i == 0.6):
            return 3
        else:
            return 4
	
    def __repr__(self):
        return self._relevances.__repr__()
	
    def __str__(self):
        return self._relevances.__str__()