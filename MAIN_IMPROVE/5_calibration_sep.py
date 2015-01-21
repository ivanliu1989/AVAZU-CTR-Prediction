# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 09:18:34 2015

@author: ivan
"""
import pandas as pd
from csv import DictReader
from datetime import datetime

train_app_path = 'data/train_df_app_smooth.csv'
train_site_path = 'data/train_df_site_smooth.csv'
test_app_path = 'data/test_df_app_smooth.csv'
test_site_path = 'data/test_df_site_smooth.csv'
submit_path = 'Blending_models_BM_CU_FM_XG_NN.csv'

test_app = pd.read_csv(test_app_path,index_col = False)
test_site = pd.read_csv(test_site_path,index_col = False)
app_id = set(test_app['id'])
site_id = set(test_site['id'])

#-- app ctr --#
'''
app_count = 0
app_sum = 0
start = datetime.now()
for t, row in enumerate(DictReader(open(train_app_path))):
    
    app_count += 1
    app_sum += float(row['click'])
    
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
app_ctr = (app_sum)/(app_count) #0.11882644017386244
'''
app_ctr = 0.11882644017386244

#-- site ctr --#            
'''
site_count = 0
site_sum = 0
start = datetime.now()
for t, row in enumerate(DictReader(open(train_site_path))):
    
    site_count += 1
    site_sum += float(row['click'])
    
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
site_ctr = (site_sum)/(site_count) #0.19861002453080054
'''
site_ctr = 0.19861002453080054

#-- test app/site ctr --#
test_count_app = 0
test_sum_app = 0
test_count_site = 0
test_sum_site = 0
start = datetime.now()
for t, row in enumerate(DictReader(open(submit_path))):
    
    ID = row['id']
    click = row['click']
    
    if ID in app_id:
        test_count_app += 1
        test_sum_app += float(row['click'])
    elif ID in site_id:
        test_count_site += 1
        test_sum_site += float(row['click'])
    elif int(ID) in app_id:
        test_count_app += 1
        test_sum_app += float(row['click'])
    elif int(ID) in site_id:
        test_count_site += 1
        test_sum_site += float(row['click'])
    else:
        break        
        
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
                        
app_ctr_test = test_sum_app/test_count_app #0.14772854946743735
site_ctr_test = test_sum_site/test_count_site #0.19105869640790787


#-- calibration diff --#
calibration_app = app_ctr - app_ctr_test
calibration_site = site_ctr - site_ctr_test

#-- calibration --#
start = datetime.now()
with open('Blending_models_BM_CU_FM_XG_NN_calibr.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(submit_path))):
        
        ID = row['id']
        click = row['click']
        
        if int(ID) in app_id:
            click = float(click) + calibration_app
        elif int(ID) in site_id:
            click = float(click) + calibration_site
        elif ID in app_id:
            click = float(click) + calibration_app
        elif ID in site_id:
            click = float(click) + calibration_site
        else:
            break 
        
        if click <= 0:
            print(click)
            
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        
        if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
         
#-- test calibration --#
test_count_app2 = 0
test_sum_app2 = 0
test_count_site2 = 0
test_sum_site2 = 0
start = datetime.now()
for t, row in enumerate(DictReader(open('pred/submit_ensemble_merge_cal_sep.csv'))):
    
    ID = row['id']
    click = row['click']
    
    if ID in app_id:
        test_count_app2 += 1
        test_sum_app2 += float(row['click'])
    elif ID in site_id:
        test_count_site2 += 1
        test_sum_site2 += float(row['click'])
    elif int(ID) in app_id:
        test_count_app2 += 1
        test_sum_app2 += float(row['click'])
    elif int(ID) in site_id:
        test_count_site2 += 1
        test_sum_site2 += float(row['click'])
    else:
        break        
        
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
                        
app_ctr_test2 = test_sum_app2/test_count_app2
site_ctr_test2 = test_sum_site2/test_count_site2 
calibration_app = app_ctr - app_ctr_test2
calibration_site = site_ctr - site_ctr_test2