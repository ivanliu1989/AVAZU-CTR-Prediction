# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 13:40:36 2015

@author: Ivan
"""
import pandas as pd
from csv import DictReader
from datetime import datetime

train_app_path = 'data/train_df_app_smooth.csv'
train_site_path = 'data/train_df_site_smooth.csv'
test_app_path = 'data/test_df_app_smooth.csv'
test_site_path = 'data/test_df_site_smooth.csv'

#-- test_app_ex --#
train_app = pd.read_csv(train_app_path,index_col = False)
del train_app['id']
del train_app['click']

hour_var = train_app['hour'].unique()
C1_var = train_app['C1'].unique()
banner_pos_var = train_app['banner_pos'].unique()
app_id_var = train_app['app_id'].unique()
app_domain_var = train_app['app_domain'].unique()
app_category_var = train_app['app_category'].unique()
device_id_var = train_app['device_id'].unique()
device_ip_var = train_app['device_ip'].unique()
device_model_var = train_app['device_model'].unique()
device_type_var = train_app['device_type'].unique()
device_conn_type_var = train_app['device_conn_type'].unique()
C14_var = train_app['C14'].unique()
C15_var = train_app['C15'].unique()
C16_var = train_app['C16'].unique()
C17_var = train_app['C17'].unique()
C18_var = train_app['C18'].unique()
C19_var = train_app['C19'].unique()
C20_var = train_app['C20'].unique()
C21_var = train_app['C21'].unique()
del train_app

start = datetime.now()
with open('data/test_df_app_smooth_ex.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test_app_path))):
        
        ID = row['id']
        hour = row['hour'][6:]
        C1 = row['C1']
        banner_pos = row['banner_pos']
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
        
        if hour not in hour_var: 
            hour = -2
        if C1 not in C1_var: 
            C1 = -2
        if banner_pos not in banner_pos_var: 
            banner_pos = -2
        if app_id not in app_id_var: 
            app_id = -2
        if app_domain not in app_domain_var: 
            app_domain = -2
        if app_category not in app_category_var: 
            app_category = -2
        if device_id not in device_id_var: 
            device_id = -2
        if device_ip not in device_ip_var: 
            device_ip = -2
        if device_model not in device_model_var: 
            device_model = -2
        if device_type not in device_type_var: 
            device_type = -2
        if device_conn_type not in device_conn_type_var: 
            device_conn_type = -2
        if C14 not in C14_var: 
            C14 = -2
        if C15 not in C15_var: 
            C15 = -2
        if C16 not in C16_var: 
            C16 = -2
        if C17 not in C17_var: 
            C17 = -2
        if C18 not in C18_var: 
            C18 = -2
        if C19 not in C19_var: 
            C19 = -2
        if C20 not in C20_var: 
            C20 = -2
        if C21 not in C21_var: 
            C21 = -2

        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))



#-- test_site_ex --#

