# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:46:43 2015

@author: ivan
"""
from datetime import datetime
from csv import DictReader
import pandas as pd

xgboost_app = 'xgboost/GBTR_D8_app.txt'
xgboost_site = 'xgboost/GBTR_D8_site.txt'
pred_app = pd.read_csv(xgboost_app,index_col = False, header = None)
pred_site = pd.read_csv(xgboost_site,index_col = False, header = None)

submit_app = 'data/test_df_app.csv'
submit_site = 'data/test_df_site.csv'
submit_app = pd.read_csv(submit_app)
submit_site = pd.read_csv(submit_site)

submission_app = pd.DataFrame({'id':submit_app['id'],
                               'click':pred_app[0]})
submission_site = pd.DataFrame({'id':submit_site['id'],
                                'click':pred_site[0]})

submission = submission_app.append(submission_site,ignore_index=True)
submission.to_csv('xgboost/submit_xgboost_app_site.csv',index=False)
