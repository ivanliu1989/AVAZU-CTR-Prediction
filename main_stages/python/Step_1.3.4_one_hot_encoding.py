# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:19:32 2015

@author: Ivan
"""
import pandas as pd
from csv import DictReader

train_path = 'data/onehot/train_df_smooth_hash_app.csv'
#test_path = 'data/onehot/test_df_smooth_hash_app.csv'
#train_path = 'data/onehot/train_df_smooth_hash_site.csv'
#test_path = 'data/onehot/test_df_smooth_hash_site.csv'
train = pd.read_csv(train_path,index_col = False)
#test = pd.read_csv(test_path,index_col = False)

#train_click_id = train[['id','click']]
del train['id']
del train['click']
#test_id = test['id']
#del test['id']

#train = train.append(test,ignore_index=True);
#del test

#-- Build dictionary --#
unique_val = pd.Series(train.values.ravel()).unique()

'''
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

all_var = hour.union(C1, banner_pos, app_id, app_domain, app_category, device_id, device_ip, device_model, device_type,
           device_conn_type, C14, C15, C16, C17, C18, C19, C20, C21)
'''

#-- Save/Read dictionary to/from csv --#
len(unique_val)

with open("data/onehot/site_var_dict.csv","wb") as outfile: #site/app
    outfile.write('key,val\n')
    for key, val in enumerate(unique_val):
        outfile.write('%s,%s\n' % (val, key))


var_dict = {}
for t, row in enumerate(DictReader(open("data/onehot/site_var_dict.csv"))): # site/app
    var_dict[row['key']] = row['val']

var_dict[str(unique_val[2000])]

#-- please find Step_1.3.5_csv2libsvm.py to continue the encoding process --#