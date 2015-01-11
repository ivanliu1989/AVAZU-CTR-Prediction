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

start = datetime.now()
with open('data/test_df_app_smooth_ex.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test_app_path))):
        
        ID = row['id']
        hour = row['hour']
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
        
        if int(hour) not in train_app['hour']: 
            hour = -2
        if int(C1) not in train_app['C1']: 
            C1 = -2
        if int(banner_pos) not in train_app['banner_pos']: 
            banner_pos = -2
        if str(app_id) not in train_app['app_id']: 
            app_id = -2
        if app_domain not in train_app['app_domain']: 
            app_domain = -2
        if app_category not in train_app['app_category']: 
            app_category = -2
        if device_id not in train_app['device_id']: 
            device_id = -2
        if device_ip not in train_app['device_ip']: 
            device_ip = -2
        if device_model not in train_app['device_model']: 
            device_model = -2
        if device_type not in train_app['device_type']: 
            device_type = -2
        if device_conn_type not in train_app['device_conn_type']: 
            device_conn_type = -2
        if C14 not in train_app['C14']: 
            C14 = -2
        if C15 not in train_app['C15']: 
            C15 = -2
        if C16 not in train_app['C16']: 
            C16 = -2
        if C17 not in train_app['C17']: 
            C17 = -2
        if C18 not in train_app['C18']: 
            C18 = -2
        if C19 not in train_app['C19']: 
            C19 = -2
        if C20 not in train_app['C20']: 
            C20 = -2
        if C21 not in train_app['C21']: 
            C21 = -2

        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))

del train_app

#-- test_site_ex --#
train_site = pd.read_csv(train_site_path,index_col = False)
del train_site['id']
del train_site['click']

start = datetime.now()
with open('data/test_df_site_smooth_ex.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,site_id,site_domain,site_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test_site_path))):
        
        ID = row['id']
        hour = row['hour'][6:]
        C1 = row['C1']
        banner_pos = row['banner_pos']
        site_id = row['site_id']
        site_domain = row['site_domain']
        site_category = row['site_category']
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
        
        if hour not in train_site['hour']: 
            hour = -2
        if C1 not in train_site['C1']: 
            C1 = -2
        if banner_pos not in train_site['banner_pos']: 
            banner_pos = -2
        if site_id not in train_site['site_id']: 
            site_id = -2
        if site_domain not in train_site['site_domain']: 
            site_domain = -2
        if site_category not in train_site['site_category']: 
            site_category = -2
        if device_id not in train_site['device_id']: 
            device_id = -2
        if device_ip not in train_site['device_ip']: 
            device_ip = -2
        if device_model not in train_site['device_model']: 
            device_model = -2
        if device_type not in train_site['device_type']: 
            device_type = -2
        if device_conn_type not in train_site['device_conn_type']: 
            device_conn_type = -2
        if C14 not in train_site['C14']: 
            C14 = -2
        if C15 not in train_site['C15']: 
            C15 = -2
        if C16 not in train_site['C16']: 
            C16 = -2
        if C17 not in train_site['C17']: 
            C17 = -2
        if C18 not in train_site['C18']: 
            C18 = -2
        if C19 not in train_site['C19']: 
            C19 = -2
        if C20 not in train_site['C20']: 
            C20 = -2
        if C21 not in train_site['C21']: 
            C21 = -2

        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))

