#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:32:07 2017
1
@author: Eleden
"""
from projet import *
from gestFile import *
from random import uniform
import json as simplejson
from Ihm.frame import *
from Ihm.env import *
import sys
import matplotlib.pyplot as plt
import pylab as pl
import matplotlib.pyplot as plt

frame = Frame()
if not frame.listRel:
    pol = frame.pol
else:
    print(frame.listRel)
    print("truc")
    gf=gestFile(frame.listRel)
    print(gf.dicOfValue.keys())
    print(gf.dicOfValue)
    mdp = mdp(8,10,gf,0.95,0.01,2000)
    [V,pol] = mdp.QLearning(0.5)       
    keys = list(gf.dicOfValue.keys())
    str1 = ''.join(str(e) for e in keys)
    frame.Type = str1
    f = open("Policies/Pol_%s.txt" % str1, 'wb')
    #np.savetxt(f,pol, delimiter=" ", fmt="%s | ") 
    np.savetxt(f,pol)
    f.close()   

#comparaison


#liste des types de menu
l = ['Relevance_Menu','SemanticMenu','UnorderedMenu']
lfile = ['BD/Menu_Alphabetic_2by4.mat','BD/Menu_Semantic_2by4.mat','BD/Menu_Unordered_2by4.mat']
time = {}
gf=gestFile(lfile)
for elem in l:
    p = compare(pol,gf,elem)
    tmp=0
    nb=10
    for i in range(nb):
        print("ITERATION ",i)
        tmp += p.getTimeToFindReward()
    time[elem] = tmp/nb
x=[]
for i in range(len(l)):
    x.append(i)
xTicks = list(time.keys())     
y = list(time.values())

pl.xticks(x, xTicks)
pl.xticks(range(len(l)), xTicks, rotation=45) 
pl.bar(x,y,color='g')
s="Temps de sélection en msd'un item pour la politique \n %s sur des menus de types différents" %frame.Type[:-4]
plt.ylabel("Temps de sélection en msd'un item pour la politique \n %s sur des menus de types différents" %frame.Type[:-4])
plt.savefig('testplot.png')
plt.show()

