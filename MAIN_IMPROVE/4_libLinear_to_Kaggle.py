# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 10:03:05 2015

@author: ivan
"""


import pandas as pd

lib_app = 'libLinear/pred/liblinear_pred_7_app.txt'
lib_site = 'libLinear/pred/liblinear_pred_7_site.txt'
pred_app = pd.read_csv(lib_app,index_col = False, header = 0, delim_whitespace=True)
pred_site = pd.read_csv(lib_site,index_col = False, header = 0, delim_whitespace=True)

submit_app = 'data/test_df_app_smooth.csv'
submit_site = 'data/test_df_site_smooth.csv'
submit_app = pd.read_csv(submit_app)
submit_site = pd.read_csv(submit_site)

submission_app = pd.DataFrame({'id':submit_app['id'],
                               'click':pred_app['1']})
submission_site = pd.DataFrame({'id':submit_site['id'],
                                'click':pred_site['1']})

submission = submission_app.append(submission_site,ignore_index=True)
submission.to_csv('libLinear_logreg_dual.csv',index=False)
