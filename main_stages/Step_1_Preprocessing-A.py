# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 10:22:58 2015

@author: ivan
"""
import pandas as pd
import numpy as np
from datetime import datetime
from csv import DictReader

train = 'data/train.csv'               # path to training file
test = 'data/test' 

# -- test data -- #
test_df = pd.read_csv(test)

test_df['dow'] = test_df['hour'].map(lambda x: str(x)[4:6])
test_df['hour'] = test_df['hour'].map(lambda x: str(x)[6:])  # 00-23
test_df['dow'] = 6                # 1,2,3,4,5,6,7
test_df['holiday'] = 1            # 1:yes 0:no 
test_df.head()
test_df['hour'].describe()

test_df.to_csv('data/test_df.csv',index=False)
test_df = pd.read_csv('data/test_df.csv')
del test_df['Unnamed: 0']
del test_df
list(test_df.columns.values)

# -- train data -- #
start = datetime.now()
with open('data/train_df.csv',"wb") as outfile:
    outfile.write('ID, click,hour,C1,banner_pos,site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21,dow,holiday\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        if row['hour'][4:6] in [19,26]:
            dow = 1
        elif row['hour'][4:6] in [20,27]:
            dow = 2
        elif row['hour'][4:6] in [21,28]:
            dow = 3
        elif row['hour'][4:6] in [22,29]:
            dow = 4
        elif row['hour'][4:6] in [23,30]:
            dow = 5
        elif row['hour'][4:6] in [18,25]:
            dow = 7
        elif row['hour'][4:6] in [24,31]:
            dow = 6
        else:
            dow = 'dow'
            
        if dow in [6,7]: # Sun sat
            holiday = 1
        elif row['hour'][4:6] == 30: # Hallowin
            holiday = 1
        else:
            holiday = 0
        
        row['hour'] = row['hour'][6:]
        
        
        outfile.write('%s,%s,%s\n' % (row, dow, holiday))
        if t % 1000000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        