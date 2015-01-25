# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 18:41:51 2015

@author: Ivan
"""

import pandas as pd

sofia_app = 'sofia-ml/pred/sofia_pred_app.txt'
sofia_site = 'sofia-ml/pred/sofia_pred_site.txt'
pred_app = pd.read_csv(sofia_app,index_col = False, header = None, delim_whitespace=True)
pred_site = pd.read_csv(sofia_site,index_col = False, header = None, delim_whitespace=True)

submission = pred_app.append(pred_site,ignore_index=True)
submission.to_csv('ftrl_0_2_3_5.csv',index=False)
