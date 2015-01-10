# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 23:23:40 2015

@author: Ivan
"""
from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt

# A, paths
train = 'data/train_df_app_smooth.csv'               # path to training file
test = 'data/test_df_app_smooth.csv'                 # path to testing file
train_s = 'data/onehot/train_df_smooth_hash_app.csv'  # path of to be outputted submission file
test_s = 'data/onehot/test_df_smooth_hash_app.csv'  # path of to be outputted submission file
D = 2**28

start = datetime.now()
with open(train_s,"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        click = row['click']
        
        hour = row['hour']
        if hour != "":
            hour = hash('hour' + hour)
            
        C1 = row['C1']
        banner_pos = row['banner_pos']
        #site_id = row['site_id']
        #site_domain = row['site_domain']
        #site_category = row['site_category']
        app_id = row['app_id']
        app_domain = row['app_domain']
        app_category = row['app_category']
        device_id = row['device_id']
        device_ip = row['device_ip']
        device_model = row['device_model']
        device_type = row['device_type']
        device_conn_type = row['device_conn_type']
        C14 = row['C14']
        C15 = row['C15']
        C16 = row['C16']
        C17 = row['C17']
        C18 = row['C18']
        C19 = row['C19']
        C20 = row['C20']
        C21 = row['C21']

        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))