# -*- coding: utf-8 -*-
"""
Created on Tue Jan 06 22:03:43 2015

@author: Ivan
"""

from datetime import datetime
from csv import DictReader
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
