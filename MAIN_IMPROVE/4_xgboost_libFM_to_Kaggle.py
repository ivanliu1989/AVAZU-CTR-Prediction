# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:46:43 2015

@author: ivan
"""
import pandas as pd

xgboost_app = 'libFM_pred_app_MCMC_900.txt'
xgboost_site = 'libFM_pred_site_MCMC_900.txt'
pred_app = pd.read_csv(xgboost_app,index_col = False, header = None)
pred_site = pd.read_csv(xgboost_site,index_col = False, header = None)

submit_app = 'data/test_df_app_smooth.csv'
submit_site = 'data/test_df_site_smooth.csv'
submit_app = pd.read_csv(submit_app)
submit_site = pd.read_csv(submit_site)

submission_app = pd.DataFrame({'id':submit_app['id'],
                               'click':pred_app[0]})
submission_site = pd.DataFrame({'id':submit_site['id'],
                                'click':pred_site[0]})

submission = submission_app.append(submission_site,ignore_index=True)
submission.to_csv('libFM_MCMC_900.csv',index=False)
