# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 22:28:22 2015

@author: Ivan.Liuyanfeng
"""
import pandas as pd

lib_app = 'MOA/naive_bayes_app_pred.csv'
lib_site = 'MOA/naive_bayes_site_pred.csv'
pred_app = pd.read_csv(lib_app,index_col = False, header = 0, delim_whitespace=False)
pred_site = pd.read_csv(lib_site,index_col = False, header = 0, delim_whitespace=False)

submit_app = 'data/test_df_app_smooth.csv'
submit_site = 'data/test_df_site_smooth.csv'
submit_app = pd.read_csv(submit_app)
submit_site = pd.read_csv(submit_site)

submission_app = pd.DataFrame({'id':submit_app['id'],
                               'click':pred_app['x']})
submission_site = pd.DataFrame({'id':submit_site['id'],
                                'click':pred_site['x']})

submission = submission_app.append(submission_site,ignore_index=True)
submission.to_csv('MOA_naive_bayes.csv',index=False)

