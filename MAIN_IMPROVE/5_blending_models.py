# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 22:32:25 2015

@author: Ivan.Liuyanfeng
"""
from datetime import datetime
from csv import DictReader
import pandas as pd

pred_file1 = 'pred/blending/submission_py_0.13_1_1_1_29_0.3931037.csv'
pred_file2 = 'pred/blending/submission_vw_cubic2_0.3957190.csv'  
pred_file3 = 'pred/blending/submit_libFM_pred_0.4027643.csv'  
pred_file4 = 'pred/blending/submit_xgboost_900_03_0.3931970.csv' 
#pred_file5 = 'pred/blending/submit_xgboost_900_03.csv'   

pred_2 = {}
for t, row in enumerate(DictReader(open(pred_file2))): # site/app
    pred_2[row['id']] = row['click']

pred_3 = {}
for t, row in enumerate(DictReader(open(pred_file3))): # site/app
    pred_3[row['id']] = row['click']

pred_4 = {}
for t, row in enumerate(DictReader(open(pred_file4))): # site/app
    pred_4[row['id']] = row['click']

'''
pred_5 = {}
for t, row in enumerate(DictReader(open(pred_file5))): # site/app
    pred_5[row['id']] = row['click']
'''

start = datetime.now()
with open('blending_min.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(pred_file1))):
        
        ID = row['id']
        click = row['click']
        #click = 3/(1/float(click) + 1/float(pred_2[ID]) + 1/float(pred_3[ID]))# + 0.25 * 2/(1/float(pred_4[ID]) + 1/float(pred_5[ID]))
        #click = 0.4*(0.7*float(click)+0.3*float(pred_4[ID])) + 0.3*float(pred_2[ID]) + 0.3*float(pred_3[ID])# + 0.3*float(pred_4[ID])
        click = min(float(click),float(pred_2[ID]),float(pred_3[ID]),float(pred_4[ID]))
        
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))