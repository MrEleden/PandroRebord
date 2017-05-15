#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:32:07 2017

@author: Eleden
"""
from projet import *
from gestFile import *
from random import uniform
import json as simplejson
from Ihm.frame import *
import sys




frame = Frame()
gf=gestFile(frame.listRel)
pol = np.genfromtxt('pol.txt')

p = compare(pol,gf)

print(p.getTimeToFindReward())

sys.exit(1)

mdp = mdp(8,10,gf,0.95,0.01,2000)


[V,pol] = mdp.QLearning(0.5)


print("taille de la police : ",len(pol))
f = open('Q.txt', 'wb')
np.savetxt(f,V, delimiter=" ", fmt="%s | ") 
f.close()

f = open('Pol.txt', 'wb')
#np.savetxt(f,pol, delimiter=" ", fmt="%s | ") 
np.savetxt(f,pol)
f.close()

