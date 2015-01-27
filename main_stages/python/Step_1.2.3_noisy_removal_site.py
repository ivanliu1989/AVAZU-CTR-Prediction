# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 08:43:51 2015
noisy removal (all unique value)
@author: ivan
"""
from collections import Counter
import pandas as pd
#from sklearn.preprocessing import OneHotEncoder

##################
# -- load data --#
##################
train = 'data/train_df_site_split.csv'               # path to training file
test = 'data/test_df_site_split.csv'
test_df = pd.read_csv(test)
train_df = pd.read_csv(train)

train_click_id = train_df[['id','click']]
del train_df['id']
del train_df['click']
test_click_id = test_df['id']
del test_df['id']

train_df = train_df.append(test_df,ignore_index=True);
del test_df

######################
# -- modification -- #
######################
df_col=list(train_df.columns.values)
    
#app_id | site_id
d = Counter(train_df[df_col[3]]) 
st = d.most_common(100000000).index(('edf9f207', 5)) #('edf9f207', 5)'a2bcbfd4', 1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[3]].isin(smooth_row),df_col[3]] = -2 # hash('other') % (2**28)

#app_domain | site_domain
d = Counter(train_df[df_col[4]]) 
st = d.most_common(100000000).index(('fba8c3cc',5)) #('fba8c3cc',5)'4378e458',1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[4]].isin(smooth_row),df_col[4]] = -2

#app_category | site_category
d = Counter(train_df[df_col[5]])#no need
st = d.most_common(100000000).index(('a72a0145',3)) #('a72a0145',3)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[5]].isin(smooth_row),df_col[5]] = -2

#device_id
d = Counter(train_df[df_col[6]]) #id dc575eb9 5
st = d.most_common(100000000).index(('ac352d50',5)) #('ac352d50',5)'a83aeb2d',1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[6]].isin(smooth_row),df_col[6]] = -2

#device_ip
d = Counter(train_df[df_col[7]]) #id #site e750d599, 5
st = d.most_common(100000000).index(('e750d599',5)) #00007a97 '00001bf2',1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[7]].isin(smooth_row),df_col[7]] = -2

#device_id2
d = Counter(train_df[df_col[8]]) #id dc575eb9 5

#device_ip2
d = Counter(train_df[df_col[9]]) #id

#device_model
d = Counter(train_df[df_col[10]])
st = d.most_common(100000000).index(('dec3afcc',5))#('dec3afcc',5)'23767ab6',1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[10]].isin(smooth_row),df_col[10]] = -2

#device_type
#d = Counter(train_df[df_col[11]]) 

#device_conn_type
#d = Counter(train_df[df_col[12]]) 

#C14
d = Counter(train_df[df_col[13]]) 
st = d.most_common(100000000).index((23576,5)) #(23576,5)7648,1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[13]].isin(smooth_row),df_col[13]] = -2

#img_size
#d = Counter(train_df[df_col[14]]) 

#C17
d = Counter(train_df[df_col[15]]) 
st = d.most_common(100000000).index((2565,3))#(2565,3)2191,1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[15]].isin(smooth_row),df_col[15]] = -2

#C18
#d = Counter(train_df[df_col[16]]) 

#C19
#d = Counter(train_df[df_col[17]]) 

#C20
d = Counter(train_df[df_col[18]]) 
st = d.most_common(100000000).index((100006,5)) #(100006,5)100209,1
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[18]].isin(smooth_row),df_col[18]] = -2

#C21
#d = Counter(train_df[df_col[19]]) 


################
# -- output -- #
################
train_df.shape
train_click_id.shape
test_click_id.shape
test_df = train_df.ix[25832830:,:]
train_df = train_df.ix[0:25832829,:]

train_df = pd.merge(train_click_id, train_df, left_index=True, right_index=True)
test_df = test_df.reset_index()
del test_df['index']
test_click_id = pd.DataFrame({'id':test_click_id})
test_df = pd.merge(test_click_id, test_df, left_index=True, right_index=True)

train_df.to_csv('data/train_df_site_split_smooth.csv',index=False)
test_df.to_csv('data/test_df_site_split_smooth.csv',index=False)