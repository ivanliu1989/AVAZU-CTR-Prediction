# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 23:26:28 2015

@author: Ivan.Liuyanfeng
"""
from collections import Counter
import pandas as pd

train = 'other/train_df_app.csv'               # path to training file
test = 'other/test_df_app.csv'
test_df = pd.read_csv(test)
train_df = pd.read_csv(train)

train_click_id = train_df[['id','click']]
del train_df['id']
del train_df['click']
test_click_id = test_df['id']
del test_df['id']

train_df = train_df.append(test_df,ignore_index=True);
del test_df

df_col=list(train_df.columns.values)

d = Counter(train_df[df_col[19]]) 
d.most_common(5)

