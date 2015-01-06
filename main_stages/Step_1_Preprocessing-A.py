# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 10:22:58 2015

@author: ivan
"""
import pandas as pd
import numpy as np
from datetime import datetime
from csv import DictReader

train = 'data/train'               # path to training file
test = 'data/test' 

# -- test data -- #
test_df = pd.read_csv(test)

test_df['dow'] = test_df['hour'].map(lambda x: str(x)[4:6])
test_df['hour'] = test_df['hour'].map(lambda x: str(x)[6:])  # 00-23
test_df['dow'] = 7                # 1,2,3,4,5,6,7
test_df['holiday'] = 1            # 1:yes 0:no 
test_df.head()
test_df['hour'].describe()

test_df.to_csv('data/test_df.csv')

# -- train data -- #

def preProcess_A(path):
    for t, row in enumerate(DictReader(open(path))):
        # turn hour really into hour, it was originally YYMMDDHH
        row['dow'] = row['hour'][4:5]
        row['hour'] = row['hour'][6:]
        
        yield row