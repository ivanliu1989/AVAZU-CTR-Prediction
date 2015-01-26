# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 08:52:33 2015

@author: Ivan
"""

from collections import Counter
import pandas as pd
#from sklearn.preprocessing import OneHotEncoder

##################
# -- load data --#
##################
train = 'data/ex/train_df_site_complete.csv'               # path to training file
test = 'data/ex/test_df_site_complete.csv'
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
  '''
#site_id | site_id
d = Counter(train_df[df_col[3]]) 
st = d.most_common(100000000).index(('07a3c559', 1)) # ('572bf9b0', 5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[3]].isin(smooth_row),df_col[3]] = -2 #hash('other') % (2**28)

#site_domain | site_domain
d = Counter(train_df[df_col[4]]) 
st = d.most_common(100000000).index(('4a4f8143',1)) # ('c91cbbb4',5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[4]].isin(smooth_row),df_col[4]] = -2

#site_category | site_category
d = Counter(train_df[df_col[5]])
st = d.most_common(100000000).index(('52de74cf',1)) #('71af18ce',5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[5]].isin(smooth_row),df_col[5]] = -2
'''
#device_id
d = Counter(train_df[df_col[6]]) #id dc575eb9 5
st = d.most_common(100000000).index(('827db5a1',3)) #('dc575eb9',5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[6]].isin(smooth_row),df_col[6]] = -2

#device_ip
d = Counter(train_df[df_col[7]]) #id
st = d.most_common(100000000).index(('3d97b194',3)) #('ff6e5da4',5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[7]].isin(smooth_row),df_col[7]] = -2
'''
#device_model
d = Counter(train_df[df_col[8]])
st = d.most_common(100000000).index(('a01422c4',1)) # ('5a33307b',5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[8]].isin(smooth_row),df_col[8]] = -2

#device_type
#d = Counter(train_df[df_col[9]]) 

#device_conn_type
#d = Counter(train_df[df_col[10]]) 

#C14
d = Counter(train_df[df_col[11]]) 
st = d.most_common(100000000).index((17027,1)) #(18467,5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[11]].isin(smooth_row),df_col[11]] = -2

#C15
#d = Counter(train_df[df_col[12]]) 

#C16
#d = Counter(train_df[df_col[13]]) 

#C17
d = Counter(train_df[df_col[14]]) 
st = d.most_common(100000000).index((2181,1))#(2206,5)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[14]].isin(smooth_row),df_col[14]] = -2

#C18
#d = Counter(train_df[df_col[15]]) 

#C19
#d = Counter(train_df[df_col[16]]) 

#C20
d = Counter(train_df[df_col[17]]) 
st = d.most_common(100000000).index((100198,1))#(100100,4)
f_list = d.most_common(100000000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
train_df.ix[train_df[df_col[17]].isin(smooth_row),df_col[17]] = -2

#C21
#d = Counter(train_df[df_col[18]]) 

'''
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

train_df.to_csv('data/train_df_site_complete.csv',index=False)
test_df.to_csv('data/test_df_site_complete.csv',index=False)