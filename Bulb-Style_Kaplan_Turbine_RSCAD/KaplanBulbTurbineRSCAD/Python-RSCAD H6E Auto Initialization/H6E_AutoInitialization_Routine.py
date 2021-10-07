# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:40:18 2021

@author: BANEA
"""



##### ask the user to input RSCAD .dft file
#print('###------------------------------------------------------------------------')
#dftfile_path = input('Enter the path for the rscad .dft file..... note: enter as a string, i.e, in between "path"')
#print('###------------------------------------------------------------------------')
#      
#
#      
      
dftfile_path = 'C:/Users/BANEA/OneDrive - Idaho National Laboratory/BRISC/American Governor models/Python-RSCAD H6E Auto Initialization/LowerBulb_Gen_Norton Current Injection_Shafiul_03.18.2021.dft';

### ----- loading .dft (RSCAD) file in python
mydftfile = []                                     # Declare an empty list.
with open (dftfile_path, 'rt') as myfile:
    for myline in myfile:                              # For each line in the file,
        mydftfile.append(myline.rstrip('\n'))      # strip newline and add to list.  