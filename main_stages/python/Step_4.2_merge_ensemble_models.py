# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 22:32:25 2015

@author: Ivan.Liuyanfeng
"""
from datetime import datetime
from csv import DictReader
import pandas as pd

pred_file1 = 'submission_py_site_app_0.13_1_1_1_s5.csv'
pred_file2 = 'submit_libFM_pred.csv'

pred_1 = {}
for t, row in enumerate(DictReader(open(pred_file1))): # site/app
    pred_1[row['id']] = row['click']
    
pred_2 = {}
for t, row in enumerate(DictReader(open(pred_file2))): # site/app
    pred_2[row['id']] = row['click']

submit1 = pd.read_csv(pred_file1)
#pred_2[submit1['id'][1]]
submit1['click2'] = 0

for key,val in enumerate(submit1['id']):
    submit1['click2'][key] = pred_2[val]
    
submit1['click'] = 0.5*submit1['click'] + 0.5*submit1['click2']
del submit1['click2']

submit1.to_csv('submit_ensemble_merge.csv',index=False)