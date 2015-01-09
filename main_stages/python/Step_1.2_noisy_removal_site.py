# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 08:43:51 2015

@author: ivan
"""
from collections import Counter
from datetime import datetime
from csv import DictReader
import pandas as pd
#from sklearn.preprocessing import OneHotEncoder
from collections import Counter

##################
# -- load data --#
##################
train = 'data/train_df_app.csv'               # path to training file
test = 'data/test_df_app.csv'
#train = 'data/train_df_site.csv'               # path to training file
#test = 'data/test_df_site.csv'
test_df = pd.read_csv(test)
train_df = pd.read_csv(train)

train_click_id = train_df[['id','click']]
del train_df['id']
del train_df['click']
test_click_id = test_df['id']
del test_df['id']

####################
# -- combine df -- #
####################
train_df = train_df.append(test_df,ignore_index=True);
del test_df

######################
# -- modification -- #
######################
df_col=list(train_df.columns.values)
    
#app_id | site_id
d = Counter(train_df[df_col[3]]) 
st = d.most_common(100000000).index(('07a3c559', 1))
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[3]].isin(smooth_row),df_col[3]] = hash('other') % (2**28)

#app_domain | site_domain
d = Counter(train_df[df_col[4]]) 
st = d.most_common(100000000).index(('4a4f8143',1))
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[4]].isin(smooth_row),df_col[4]] = hash('other') % (2**28)

#app_category | site_category
d = Counter(train_df[df_col[5]]) 
st = d.most_common(100000000).index(('4a4f8143',1))
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[5]].isin(smooth_row),df_col[5]] = hash('other') % (2**28)

#device_id
d = Counter(train_df[df_col[6]]) 
st = d.most_common(100000000).index(('4a4f8143',1))
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[6]].isin(smooth_row),df_col[6]] = hash('other') % (2**28)


d = Counter(train_df[df_col[7]]) #device_ip
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[8]]) #device_model
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[9]]) #device_type
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[10]]) #device_conn_type
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[11]]) #C14
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[12]]) #C15
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[13]]) #C16
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[14]]) #C17
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[15]]) #C18
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[16]]) #C19
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[17]]) #C20
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[18]]) #C21
result = [a for a, b in enumerate(d.values()) if b <=5]


################
# -- output -- #
################
train_df.shape
test_df = comb_df.ix[40428967:,:]
del com_df.ix[40428967:,:]

pd.merge(train_click_id, com_df)
pd.merge(test_click_id, test_df)

train_click_id.to_csv('data/train_df_app_smooth.csv',index=False)
test_click_id.to_csv('data/test_df_app_smooth.csv',index=False)