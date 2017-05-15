# -*- coding: utf-8 -*-
"""
Created on Mon May 15 03:30:59 2017

@author: Eleden
"""

import numpy as np
from plot import compare

frame = Frame()
gf=gestFile(frame.listRel)

#pol = np.loadtxt('pol.txt', delimiter=' | ')
pol = np.genfromtxt('../pol.txt')

p = compare(pol)
