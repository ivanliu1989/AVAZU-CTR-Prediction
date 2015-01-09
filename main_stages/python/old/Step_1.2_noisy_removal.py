# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 12:53:31 2015

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
# del train_df
del test_df
#train_df[df_col[0]].apply(pd.value_counts)
######################
# -- modification -- #
######################
df_col=list(train_df.columns.values)
#enc = OneHotEncoder()
#enc.fit(test_df[['C1','banner_pos']])
#a= enc.transform(test_df[['C1','banner_pos']])
#b = pd.DataFrame(a)                               
#train_df['counts'] = train_df.groupby(['hour']).transform(len)
#test_df.ix[(test_df.counts <= 5),'hour'] = hash('hour'+_+'other')%(2**28) # ??

d = Counter(train_df[df_col[3]]) #app_id | site_id
st = d.most_common(100000).index(('07a3c559', 1))
f_list = d.most_common(10000)[st:] 
smooth_row = []
for a in f_list:
    smooth_row.append(a[0])
for r in train_df[df_col[3]]:
    if r in smooth_row:
        r = hash('other') % (2**28)

d = Counter(train_df[df_col[4]]) #app_domain | site_domain
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[5]]) #app_category | site_category
result = [a for a, b in enumerate(d.values()) if b <=5]

d = Counter(train_df[df_col[6]]) #device_id
result = [a for a, b in enumerate(d.values()) if b <=5]

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

# df_freq = lambda x: Counter(train_df[x])
# df_freq('hour')
# hash('other') % (10**6)

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