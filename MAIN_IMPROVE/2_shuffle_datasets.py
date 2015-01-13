# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:36:06 2015

@author: ivan
"""
import pandas as pd
import numpy as np

train_app_path = 'data/train_df_app_smooth.csv'
train_app = pd.read_csv(train_app_path,index_col = False)

train_app = train_app.reindex(np.random.permutation(train_app.index))
#train_app = train_app.iloc(np.random.permutation(train_app.index))
train_app.to_csv('train_df_app_smooth_shuffled.csv',index=False)


train_site_path = 'data/train_df_site_smooth.csv'
train_site = pd.read_csv(train_site_path,index_col = False)

train_site = train_site.reindex(np.random.permutation(train_site.index))
#train_app = train_app.iloc(np.random.permutation(train_app.index))
train_site.to_csv('train_df_site_smooth_shuffled.csv',index=False)
