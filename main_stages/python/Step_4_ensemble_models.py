# -*- coding: utf-8 -*-
"""
Created on Tue Jan 06 22:03:43 2015

@author: Ivan
"""
import pandas as pd

xgboost_file = 'ensemble/submit_xgboost_005.csv'
vw_file = 'ensemble/submission.csv'
python_file = 'ensemble/submission_0391100.csv'

xgboost_pred = pd.read_csv(xgboost_file)
vw_pred = pd.read_csv(vw_file)
python_pred = pd.read_csv(python_file)

submit_file = 'xgboost/submission.csv'
submit = pd.read_csv(submit_file)

submit['click'] = 0.5*python_pred['click'] + 0.5*vw_pred['click']# + 0.3*xgboost_pred['click']
submit.to_csv('submit_ensemble_3.csv',index=False)


## xgboost trees ##
xgboost_file1 = 'xgboost/submit_xgboost_app_site_1.csv'
xgboost_file2 = 'xgboost/submit_xgboost_app_site_2.csv'
xgboost_file3 = 'xgboost/submit_xgboost_app_site_3.csv'
xgboost_file4 = 'xgboost/submit_xgboost_app_site_4.csv'

xgboost_pred1 = pd.read_csv(xgboost_file1)
xgboost_pred2 = pd.read_csv(xgboost_file2)
xgboost_pred3 = pd.read_csv(xgboost_file3)
xgboost_pred4 = pd.read_csv(xgboost_file4)

submit = pd.read_csv(xgboost_file1)

submit['click'] = (xgboost_pred1['click'] + xgboost_pred2['click'] + xgboost_pred3['click'] +xgboost_pred4['click'])/4
submit.to_csv('submit_ensemble_4.csv',index=False)
