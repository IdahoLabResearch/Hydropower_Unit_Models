# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:35:04 2021

@author: Abhishek Banerjee
Version: 1.0
"""


##### ------ Load data script -----

mbase = 8.9;                         # generator MVA base
tbase = 8.3;                         # turbine real power base, MW
h   = 0.83;                          # rotating inertia constant
tpe = 0.5;                          # governor elec. power detector t.c.
tsp = 0.05;                         # governor speed detector time constant
fd = 0;                             # 0 for speed mode, 1 for load mode
re = .05;                           # governor droop - load control mode
# td = .05;                         # derivative gain filter tie constant
kg = 5;                             # gate servo pilot gain
tg = 0.05;                          # gate servo pilot tc
velm = 0.2;                         # gate velocity limit
gmax = 1;                           # max gate stroke
gmin = 0;                           # min gate stroke
dturb = 0.5;                        # turbine damping at g=1
pgc = 0.0;                          # motoring power at g=0                                              
hdam = 1.0;                         # available head
deff = 1.0;                         # off-cam efficiency penalty factor
buf = 0.1;                          # top of buffer region
buv = 0.03;                         # buffer gate closing rate
tw  = 3;                            # water inertia time constant
tbd = 0.;                           # blade pilot servo time constant
tbs = 0.;                           # blade servo time constant
dbbd = 0.0;                         # deliberate blade cam deadband
dbbs = 0.0;                         # blade servo mechanical deadband
blg  = 0.0;                         # gate lineage backlash
blb  = 0.0;                         # blade linkage backlash
bvlm = 1.01;                        # blade servo velocity limit
bgvmin = .8;                        # turbine flow factor as min blade stroke


#from array import array
ggv = [0,30,40,50,60,70,80,90,95,100];
ggv_base = 100;
ggv = [i/ggv_base for i in ggv];
#ggv = numpy.array(ggv)

pgv = [-.4, 1.63, 2.35, 2.98, 3.61, 4.95, 5.98, 6.68, 6.75, 6.8];
pgv_base = 8.3;
pgv = [i/pgv_base for i in pgv];
#pgv = numpy.array(pgv)

bgv = [0, 9.50, 16.0, 22.5, 30.0, 53.5, 77.1, 87.6, 93.0, 100];
bgv_base = 100;
bgv = [i/bgv_base for i in bgv];
#bgv = numpy.array(bgv)





#### ------ PID governor settings ---
########  =============  override standard model parameters as appropriate (when
########  in isolated mode of operation) [December 2017 Field Test/ Matt Roberts]==========


##### == 1MW + load steps ==
pinit  = 2;                          
plocal = 2;
bbias = -.0;

ke=0;
delec = 0.0;
bbias = -.0

rg = 0;                           # governor droop - speed cpntrol mode
td = 0.05;                        # derivative gain filter tie constant

kp=1.35;
ki=0.2;
kd=0.75;

    

        