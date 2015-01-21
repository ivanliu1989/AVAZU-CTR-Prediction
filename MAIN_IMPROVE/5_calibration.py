# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 09:18:34 2015

@author: ivan
"""
from csv import DictReader
from datetime import datetime

#train_app_path = 'data/train_df_app_smooth.csv'

#train_site_path = 'data/train_df_site_smooth.csv'

submit_path = 'Blending_models_BM_CU_FM_XG_NN.csv'
'''
app_count = 0
app_sum = 0
start = datetime.now()
for t, row in enumerate(DictReader(open(train_app_path))):
    
    app_count += 1
    app_sum += float(row['click'])
    
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
            

site_count = 0
site_sum = 0
start = datetime.now()
for t, row in enumerate(DictReader(open(train_site_path))):
    
    site_count += 1
    site_sum += float(row['click'])
    
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            

average_ctr = (app_sum+site_sum)/(app_count+site_count) #0.16980562476404604
'''
average_ctr = 0.16980562476404604

test_count = 0
test_sum = 0
start = datetime.now()
for t, row in enumerate(DictReader(open(submit_path))):
    
    test_count += 1
    test_sum += float(row['click'])
    
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
            
average_ctr_test = test_sum/test_count

calibration = average_ctr - average_ctr_test

#-- calibration --#
start = datetime.now()
with open('Blending_models_BM_CU_FM_XG_NN_calibr.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(submit_path))):
        
        ID = row['id']
        click = row['click']
        click = float(click) + calibration/2
        
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        
        if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
         
#-- testing --#
test_count = 0
test_sum = 0
start = datetime.now()
for t, row in enumerate(DictReader(open('Blendling_lg_gbt_fm_cubic_calibr.csv'))):
    
    test_count += 1
    test_sum += float(row['click'])
    
    if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
            
average_ctr_test = test_sum/test_count

calibration = average_ctr - average_ctr_test