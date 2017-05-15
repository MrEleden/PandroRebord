# -*- coding: utf-8 -*-
"""
Created on Mon May 15 03:30:59 2017

@author: Eleden
"""

import numpy as np


#pol = np.loadtxt('pol.txt', delimiter=' | ')
pol = np.genfromtxt('../pol.txt')
print(pol)

a = [0,0,1,0,0,1]
s = "".join(map(str, a))
s=  int(s, base=2)


[int(x) for x in bin(8)[2:]]