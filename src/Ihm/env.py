# -*- coding: utf-8 -*-
"""
Created on Mon May 15 02:03:43 2017

@author: Eleden
"""
import numpy as np
from random import uniform

class compare():
    
    
    def __init__(self,policy,gf,menuType):
        self.policy=policy
        self.menuType = menuType
        self.gf=gf
    
    def getTimeToFindReward(self):
        self.choix = np.random.randint(len(self.gf.dicOfValue[self.menuType])-1)
        self.state = [0,0,0,0,0,0,0,0] 
        self.time=0.0
        self.lastItem=0
        self.finalState=False
        while(not self.finalState):
            
            u = int(self.policy[self.stateToId(self.state)])
            print("action avt test ",u)
            if(u == self.lastItem):
                print("same action !")
                for i in range(len(self.state)):
                    if self.state[i] == 0:
                        u=i
                        break
                
            print("je fait l'action :",u," depuis l'état ",self.state)
            self.doActionInState(u)
           
            self.time = self.time + 437 +( 2.7 * np.abs(self.lastItem-u))
            self.lastItem = u
            print("j'arrrive dans l'état : ",self.state," avec un temps de :",self.time )
            
        
        return self.time
    
    
    def doActionInState(self,u):
        k=u
        if u>7:
            k=self.lastItem
        if self.gf.dicOfValue[self.menuType][self.choix][k] == 1:
            self.finalState=True;
            print("Bonne réponse trouvée")
        if u ==9:
            print("sorti du menu")
            #on considère une sortie de menu comme une mauvaise action
            self.finalState=True
        if self.stateToId(self.state) == 255:
            self.finalState=True
        self.state[k]=1;
    
    
    def stateToId(self,state):
        s = "".join(map(str, state))
        return int(s, base=2)
    
    def idToState(self,id):
        a=[int(x) for x in bin(id)[2:]]
        a.reverse()
        while len(a)<8: 
            a.append(0)
        a.reverse()