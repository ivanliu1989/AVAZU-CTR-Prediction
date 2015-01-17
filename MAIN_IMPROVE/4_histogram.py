# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 22:35:35 2015

@author: Ivan.Liuyanfeng
"""
#((#nclick+ alpha *0.25)/(#ncount+alpha)) of CTR(alpha=10)

import pandas as pd

alpha = 10

train_site_path = 'data/train_df_site_smooth.csv'
test_site_path = 'data/test_df_site_smooth.csv'

train_site = pd.read_csv(train_site_path,index_col = False)
test_site = pd.read_csv(test_site_path,index_col = False)

train_site.groupby('hour').sum()['click']
train_site.groupby('hour').count()['click']

train_site_hour = (train_site[['hour','click']].groupby('hour').sum()['click'] + alpha*0.25)/(train_site[['hour','click']].groupby('hour').count()['click']
 + 10)
train_site_C1 = (train_site[['C1','click']].groupby('C1').sum()['click'] + alpha*0.25)/(train_site[['C1','click']].groupby('C1').count()['click']
 + 10)
 
