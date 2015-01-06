# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 08:43:51 2015

@author: ivan
"""

from collections import Counter
from datetime import datetime
from csv import DictReader
import pandas as pd

train = 'data/train_df.csv'               # path to training file
test = 'data/test_df.csv'

# -- test --#
test_df = pd.read_csv(test)

test_df.head()
test_col = list(test_df.columns.values)

test_freq = lambda x: Counter(test_df[x])

for col in test_col:
    if col in ['id','click','site_id','app_id','device_id']:
        continue
    print(col)
    print(test_freq(col))

# modification
test_freq('hour')
test_df.ix[(test_df.hour == 6),'hour'] = 25

# hash('other') % (10**6)
# hash('other') % (2**28)

###############
# -- train -- #
###############
train_df = pd.read_csv(train)

train_df.head()
train_col = list(train_df.columns.values)

train_freq = lambda x: Counter(train_df[x])

train_freq('click')

train_df[(train_df.click == 6)]['click'] = ''


