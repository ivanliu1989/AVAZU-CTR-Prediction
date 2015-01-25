# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 18:57:29 2015

@author: Ivan
"""

import pandas as pd

train = 'data/smooth/train_df_site_smooth.csv'               # path to training file
test = 'data/smooth/test_df_site_smooth.csv'                 # path to testing file
train2 = 'data/smooth/train_df_app_smooth.csv'               # path to training file
test2 = 'data/smooth/test_df_app_smooth.csv'                 # path to testing file

train_dt = pd.read_csv(train,index_col = False, delim_whitespace=False)
del train_dt['dow']
train_dt.to_csv('train_df_site_smooth.csv',index=False)

del train_dt

test_dt = pd.read_csv(test,index_col = False, delim_whitespace=False)
del test_dt['dow']
test_dt.to_csv('test_df_site_smooth.csv',index=False)

del test_dt

train_dt2 = pd.read_csv(train2,index_col = False, delim_whitespace=False)
test_dt2 = pd.read_csv(test2,index_col = False, delim_whitespace=False)

del train_dt2['dow']
del test_dt2['dow']

train_dt2.to_csv('train_df_app_smooth.csv',index=False)
test_dt2.to_csv('test_df_app_smooth.csv',index=False)



