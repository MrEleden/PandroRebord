# -*- coding: utf-8 -*-
"""
Created on Mon May 15 02:03:43 2017

@author: Eleden
"""
import numpy as np
from random import uniform

class compare():
    
    
    def __init__(self,policy,gf):
        self.policy=policy
        self.state = [0,0,0,0,0,0,0,0]    
        self.gf=gf
        self.finalState=False
        self.time=0.0
        self.lastItem=0
    
    def getTimeToFindReward(self):
        self.choix = np.random.randint(len(self.gf.dicOfValue['SemanticMenu'])-1)
        while(not self.finalState):
            u = int(self.policy[self.stateToId(self.state)])
            self.doActionInState(u)
            self.time = self.time + 437 +( 2.7 * np.abs(self.lastItem-u))
        
        return self.time
    
    
    def doActionInState(self,u):
        k=u
        if u>7:
            k=7
        if self.gf.dicOfValue['SemanticMenu'][self.choix][k] == 1:
            self.finalState=True;
            
        self.state[u]=1;
    
    
    def stateToId(self,state):
        s = "".join(map(str, state))
        return int(s, base=2)
    
    def idToState(self,id):
        a=[int(x) for x in bin(id)[2:]]
        a.reverse()
        while len(a)<8: 
            a.append(0)
        a.reverse()