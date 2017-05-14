#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:25:24 2017

@author: Eleden
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



class mdp():
    
    def __init__(self,nbetat,nbactions):
        self.ne=nbetat
        self.na=nbactions