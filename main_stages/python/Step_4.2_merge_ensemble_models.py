# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 22:32:25 2015

@author: Ivan.Liuyanfeng
"""
from datetime import datetime
from csv import DictReader
import pandas as pd

pred_file1 = 'submission_py_site_app_0.13_1_1_1_s5.csv'
pred_file2 = 'submit_xgboost_app_site.csv'  
pred_file3 = 'submit_libFM_pred.csv'  

pred_2 = {}
for t, row in enumerate(DictReader(open(pred_file2))): # site/app
    pred_2[row['id']] = row['click']

pred_3 = {}
for t, row in enumerate(DictReader(open(pred_file3))): # site/app
    pred_3[row['id']] = row['click']

start = datetime.now()
with open('submit_ensemble_merge.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(pred_file1))):
        
        ID = row['id']
        click = row['click']
        click = 0.4*float(click) + 0.4*float(pred_2[ID]) + 0.2*float(pred_3[ID])
        
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
        
