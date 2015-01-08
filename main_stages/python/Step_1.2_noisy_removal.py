# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 08:43:51 2015

@author: ivan
"""
from collections import Counter
from datetime import datetime
from csv import DictReader
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
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
d = Counter(train_df['hour'])
d_s = d[d<=5]
n, m = d.keys(), d.values()
print n, m
# df_freq = lambda x: Counter(train_df[x])
# df_freq('hour')
# hash('other') % (10**6)

################
# -- output -- #
################
test_df = comb_df.ix[40428967:,:]
del com_df.ix[40428967:,:]

pd.merge(train_click_id, com_df)
pd.merge(test_click_id, test_df)

train_click_id.to_csv('data/train_df_clean.csv',index=False)
test_click_id.to_csv('data/test_df_clean.csv',index=False)