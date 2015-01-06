# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:46:43 2015

@author: ivan
"""
import pandas as pd
import numpy as np
from datetime import datetime
from csv import DictReader

# --- Transform func --- #
def construct_line(line):
    new_line = []
    
    if line['click'] == '0':
        label = "0"
    elif line['click'] == '1':
        label = "1"
    else:
        break
    
    new_line.append(label)
    
    for i, item in enumerate(line):
        if item == '' or float( item ) == 0.0:
            continue
        new_item = "%s:%s" % ( i + 1, item )
        new_line.append( new_item )
    new_line = " ".join( new_line )
    new_line += "\n"
    return new_line


# --- Main transformation --- #
input_file = 'data/train_df.csv'
output_file = 'data/libsvm_train.txt'

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        
        
        new_line = construct_line(row)
        
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
        outfile.write(new_line)
    
    
    
    
