# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 09:26:49 2015

@author: ivan
"""

import pandas as pd

sofia_app = 'sofia_app_pred_logreg_sto_01'
sofia_site = 'sofia_site_pred_logreg_sto_01'
pred_app = pd.read_csv(sofia_app,index_col = False, header = None, delim_whitespace=True)
pred_site = pd.read_csv(sofia_site,index_col = False, header = None, delim_whitespace=True)

submit_app = 'data/test_df_app_smooth.csv'
submit_site = 'data/test_df_site_smooth.csv'
submit_app = pd.read_csv(submit_app)
submit_site = pd.read_csv(submit_site)

submission_app = pd.DataFrame({'id':submit_app['id'],
                               'click':pred_app[0]})
submission_site = pd.DataFrame({'id':submit_site['id'],
                                'click':pred_site[0]})

submission = submission_app.append(submission_site,ignore_index=True)
submission.to_csv('sofia_logreg_sto_01.csv',index=False)
