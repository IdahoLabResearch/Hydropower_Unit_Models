# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:43:32 2021

@author: BANEA
"""

def interp(a,x,y,n):
    
    z=0;
    
    if (a>x[n]):
        z = y[n] 
        return z
    
    if  (a<=x[0]) :
        z = y[0];
        return z;
        
    for i in range(n):
        if (a<=x[i+1]):
            z = y[i] + ((a-x[i])*((y[i+1]-y[i])/(x[i+1]-x[i])))
            return z

    
    
        
        