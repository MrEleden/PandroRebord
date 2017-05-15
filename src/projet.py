#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:25:24 2017

@author: Eleden
"""

import numpy as np
from gestFile import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from model.actions import Actions
from model.qvalues import QValues
from model.States import States
from model.menu import Menu
from random import uniform
from model.reward import Reward
from model.proba import Proba


VALUE = 2

class mdp():
    
    def __init__(self,nbitems,nbactions,gestFile,gamma,alpha,nbIter):
      
        self.ne=(VALUE**nbitems)#*nbitems
       
        self.na=nbactions
        self.gf = gestFile
        self.nbIter = nbIter
        self.alpha = alpha
        self.gamma=gamma
        #init proba
        self.P = Proba(self.ne)
        self.r = np.zeros((self.ne, self.na))
        
        
       
        
         
    def MDPStep(self,x,u):
        #choix d'un etat par rapport a une probabilité sur une action
        temp = []
        for i in np.arange(0.0,self.ne,1.0):
            temp.append(self.P[x,u,i])
        tab = np.array(temp)
        y = self.discreteProb(tab.reshape(self.ne,1))
        r = self.reward(x,u) + 0.1*np.random.randn()
        
        return [y,r]
        
    def discreteProb(self,p):
        r = np.random.random()
        cumprob=np.hstack((np.zeros(1),p.cumsum()))
        sample = -1
        for j in range(p.size):
            if (r>cumprob[j]) & (r<=cumprob[j+1]):
                sample = j
                break
        return sample
    

    def softmax(self,Q,x,tau):
        tauQ = np.exp(Q[x]/tau)
        p = tauQ / tauQ.sum()
        return p

    
    def QLearning(self,tau):
        Q = np.zeros((self.ne,self.na))
        #Q = QValues()
        #np.savetxt('dump.txt',Q)
        for i in range(self.nbIter):
            u=0
            self.choix = np.random.randint(len(self.gf.dicOfValue[list(self.gf.dicOfValue.keys())[0]])-1)
            #Q = np.genfromtxt('dump.txt')
            while(u<8):
                 print('iteration ',i)
                 x = np.floor(self.ne*np.random.random())
                 u = self.discreteProb(self.softmax(Q,x,tau))
                 [y,r] = self.MDPStep(x,u)
                 print("pour l'état ",x,"d'action : ",u,"je vais dans l'état :",y)
                 Q[x,u] = Q[x,u] + self.alpha * (r + self.gamma * Q[y,:].max() - Q[x,u])
            #np.savetxt('dump.txt',Q)
                 
        
        Qmax = Q.max(axis=1)
        pol =  np.argmax(Q,axis=1)
        return [Qmax,pol]
    
    def reward(self,state,action):
        time = 437# +( 2.7 * np.abs(lastaction-action))
        score = -10000
        k=action
        if action>7:
            k=7
        print(self.choix,k)
        if self.gf.dicOfValue[list(self.gf.dicOfValue.keys())[0]][self.choix][k] == 1:
            score = 10000
        value = score - time
        self.r[state,action] = value  
        return value
    