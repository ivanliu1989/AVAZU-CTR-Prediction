# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:19:32 2015

@author: Ivan
"""
import pandas as pd

train_path = 'data/onehot/train_df_smooth_hash_app.csv'
test_path = 'data/test_df_smooth_hash_app.csv'
train = pd.read_csv(train_path,index_col = False)
test = pd.read_csv(test_path,index_col = False)

train_click_id = train[['id','click']]
del train['id']
del train['click']
test_id = test['id']
del test['id']

train = train.append(test,ignore_index=True);
del test

# --Build dictionary-- #
hour = set(list(train['hour']))
C1 = set(list(train['C1']))
banner_pos = set(list(train['banner_pos']))
app_id = set(list(train['app_id']))
app_domain = set(list(train['app_domain']))
app_category = set(list(train['app_category']))
device_id = set(list(train['device_id']))
device_ip = set(list(train['device_ip']))
device_model = set(list(train['device_model']))
device_type = set(list(train['device_type']))
device_conn_type = set(list(train['device_conn_type']))
C14 = set(list(train['C14']))
C15 = set(list(train['C15']))
C16 = set(list(train['C16']))
C17 = set(list(train['C17']))
C18 = set(list(train['C18']))
C19 = set(list(train['C19']))
C20 = set(list(train['C20']))
C21 = set(list(train['C21']))

all_v = hour.union(C1, banner_pos, app_id, app_domain, app_category, device_id, device_ip, device_model, device_type,
           device_conn_type, C14, C15, C16, C17, C18, C19, C20, C21)

d = dict((key, i) for i, key in enumerate(all_v))
