# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 08:42:49 2015

@author: ivan
"""
import pandas as pd
from sklearn.naive_bayes import GaussianNB

train_app_path = 'data/train_df_app_smooth.csv'
test_app_path = 'data/test_df_app_smooth.csv'
train_app = pd.read_csv(train_app_path,index_col = False)
test_app = pd.read_csv(test_app_path,index_col = False)
app_target = train_app['click']
del train_app['click']
del train_app['id']
test_id = test_app['id']
del test_app['id']

gnb = GaussianNB()
fit_app = gnb.fit(train_app, app_target)
pred_app = fit_app.predict(test_app)