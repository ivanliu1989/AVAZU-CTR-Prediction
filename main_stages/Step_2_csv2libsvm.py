# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:46:43 2015

@author: ivan
"""
import pandas as pd
import numpy as np
from datetime import datetime
from csv import DictReader


# --- Main transformation --- #
input_file = 'data/train_df.csv'
output_file = 'xgboost/libsvm_train.txt'

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
    
        if row[' click'] == '0':
            label = 0
        elif row[' click'] == '1':
            label = 1
        else:
            break
        
        new_line.append(label)
        
        for i, item in row.items():
            index = hash(item)
            if index == '' or float(index) == 0.0 or i in ["id"," click"]:
                continue
            new_item = "%s:%s" % ( i+1, index )
            new_line.append( new_item )
            new_line = " ".join( new_line )
            new_line += "\n"
        
        outfile.write(new_line)
        
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
        
test_df = pd.read_csv('data/test_df.csv')    
    
    
    
