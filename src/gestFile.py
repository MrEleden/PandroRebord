#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:47:54 2017

@author: Eleden
"""
import scipy.io


class gestFile(object):
    
    
    def __init__(self,file_name):
        self.dicOfValue= {}
        for i in range(len(file_name)):
            temp = scipy.io.loadmat(file_name[i])
            keys = list(temp.keys())
            relevance_name = keys[3]
            self.dicOfValue[relevance_name]=temp[relevance_name]

        self.normalisation()
            
    def normalisation(self):
        for value in self.dicOfValue.values():
            for i in range(len(value)):
               for j in range(len(value[i])):
                   val = value[i][j]
                   if(val <1):
                       if val<0.15:
                           value[i][j]=0.0
                       elif val<0.50:
                           value[i][j]=0.3
                       elif val<0.85:
                           value[i][j]=0.5
                       else:
                            value[i][j]=0.7

                
                           
                           
                           
                           
                           
                           
                           
                           
                           
