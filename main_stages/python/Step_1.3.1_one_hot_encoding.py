# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:19:32 2015

@author: Ivan
"""
import numpy as np
import pandas as pd
from OneHotEncoder_2 import OneHotEncoderCOO as enc

train_path = 'data/train_df_app_smooth.csv'
test_path = 'data/test_df_app_smooth.csv'
train = pd.read_csv(train_path,index_col = False)
test = pd.read_csv(test_path,index_col = False)

train_click_id = train[['id','click']]
del train['id']
del train['click']
test_id = test['id']
del test['id']

train = train.append(test,ignore_index=True);
del test

test_oh = oh.keymap

enc_test = enc()
ent_fit = enc_test.fit(train)
ent_trans = enc.transform(train)

train.head()
