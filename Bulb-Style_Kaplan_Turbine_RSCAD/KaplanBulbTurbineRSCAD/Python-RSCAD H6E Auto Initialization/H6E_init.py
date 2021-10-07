# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import re
import math
from interpolation import interp
from H6E_LoadData import *




########## -------- Initialization Code ------------
qgv_arr=[];
for i in range(0, 10):                                      # build flow-area versus gate table 
#    print('Hello')
    qgv = ggv[i] * (bgvmin+(1-bgvmin)*bgv[i]);
    qgv_arr.append(qgv)
    
pelec = pinit/mbase                                 # scale elec power to generator Mbase
pmech = pinit/tbase                                 # scale mech power to turbine Tbase    

dtp = deff*bbias*bbias                              # apply off-cam power decrememnt
pmt = pmech + dtp
    
    

flow = interp(pmt,pgv,qgv_arr,9)   
    

i_s = -1;
a = 0;

if ((pmt/hdam) < pgv[1]):
    i_s = 1;
    a = 0;
    g = ggv[1] + ((pmt/hdam)-pgv[1])*(ggv[2]-ggv[1])/(pgv[2]-pgv[1])
    
else:
    for i in range(1,10):
        if ((pmt/hdam >= pgv[i-1]) & (pmt/hdam <= pgv[i])):
            d = ggv[i-1];                                       
            e = bgv[i-1];
            a = (bgv[i] - bgv[i-1]) / (ggv[i] - ggv[i-1]);
            i_s = i;
            break;
            

if (i_s<0):
    print("Overloaded")
                    
B = bgvmin                                                  # solve the quadratic for gate opening
A = 1 - B;            
        
        
if (a>0):
    aqc = A * a
    bqc = B + A*e - A*a*d + A*bbias
    cqc = - flow / math.sqrt(hdam)
    g = (-bqc+math.sqrt(bqc*bqc-4*aqc*cqc))/(2*aqc)
    
    bb = interp(g, ggv, bgv, 9);
    print("Blade initialized at bb =  ", bb);
    
else:
    print("Found flat blade segment");
    g = interp(flow/math.sqrt(hdam), qgv, ggv,9);             # g is estimate of gate opening
    
    
    
for i in range(9):                                                      # refine the gate estimate in case gate and
    bc = bgvmin + (1-bgvmin) * (interp(g, ggv, bgv,9)+bbias);      # blade lie on different segments
    af = g * bc;                                                    # (do 5 iterations)
    flow = math.sqrt(hdam)*af;                                           # (Iterate on g)
    ph = hdam * interp(flow, qgv_arr, pgv, 9);
    print(g,bc,flow);
    g = g + 0.9*(pmt-ph);


gout = g;    
    

# initialize state variables

s8 = flow;
s4 = 0;
s5 = g;  

s7 = bb;                            
bb = s7;  
s6 = s7; 
bh = s7;                        

gv = g;

hscroll = hdam;
pref = 1;
s9 = pinit/tbase;


s1 = 1;


##### -------- Initializing Pref ------    
if (fd>0):
    pref = 1 + s9 * re;  
elif (fd == 0):
    pref = 1 + gout * rg;     


##### -------- Initializing Integral gain for governor ------    
s2 = 0;   
if (fd>0):
    s2 = gout - kp * (pref - 1);
elif (fd == 0): 
    s2 = gout - kp * (pref - 1 - rg * gout);

s3 = 0;

s10 = 1;


if (ke>0):
    s11 = (pinit/mbase - plocal/mbase)/ke;
else:
    s11 = 0;
    
    
    # ------ the internal states are -----
s = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11];

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

   















