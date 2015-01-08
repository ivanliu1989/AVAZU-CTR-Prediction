# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 14:40:24 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

train = 'data/train.csv'               # path to training file
test = 'data/test.csv' 

# -- train data -- #
# list(test_df.columns.values)

start = datetime.now()
with open('data/train_df_null.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        click = row['click']
        hour = row['hour'][6:]
        C1 = row['C1']
        banner_pos = row['banner_pos']
        site_id = row['site_id']
        site_domain = row['site_domain']
        site_category = row['site_category']
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
        
        if ID in ['d41d8cd9']: 
            ID = None
        if click in ['d41d8cd9']: 
            click = None
        if hour in ['d41d8cd9']: 
            hour = None
        if C1 in ['d41d8cd9']: 
            C1 = None
        if banner_pos in ['d41d8cd9']: 
            banner_pos = None
        if site_id in ['d41d8cd9', '85f751fd']: 
            site_id = None
        if site_domain in ['d41d8cd9','c4e18dd6']: 
            site_domain = None
        if site_category in ['d41d8cd9','50e219e0']: 
            site_category = None
        if app_id in ['d41d8cd9','ecad2386']: 
            app_id = None
        if app_domain in ['d41d8cd9','7801e8d9']: 
            app_domain = None
        if app_category in ['d41d8cd9','07d7df22']: 
            app_category = None
        if device_id in ['d41d8cd9']: 
            device_id = None
        if device_ip in ['d41d8cd9']: 
            device_ip = None
        if device_model in ['d41d8cd9']: 
            device_model = None
        if device_type in ['d41d8cd9']: 
            device_type = None
        if device_conn_type in ['d41d8cd9']: 
            device_conn_type = None
        if C14 in ['d41d8cd9']: 
            C14 = None
        if C15 in ['d41d8cd9']: 
            C15 = None
        if C16 in ['d41d8cd9']: 
            C16 = None
        if C17 in ['d41d8cd9']: 
            C17 = None
        if C18 in ['d41d8cd9']: 
            C18 = None
        if C19 in ['d41d8cd9']: 
            C19 = None
        if C20 in ['d41d8cd9']: 
            C20 = None
        if C21 in ['d41d8cd9']: 
            C21 = None

        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
        
 # -- test data -- #
start = datetime.now()
with open('data/test_df_null.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test))):
         
        ID = row['id']
        hour = row['hour'][6:]
        C1 = row['C1']
        banner_pos = row['banner_pos']
        site_id = row['site_id']
        site_domain = row['site_domain']
        site_category = row['site_category']
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
        
        if ID in ['d41d8cd9']: 
            ID = None
        if hour in ['d41d8cd9']: 
            hour = None
        if C1 in ['d41d8cd9']: 
            C1 = None
        if banner_pos in ['d41d8cd9']: 
            banner_pos = None
        if site_id in ['d41d8cd9', '85f751fd']: 
            site_id = None
        if site_domain in ['d41d8cd9','c4e18dd6']: 
            site_domain = None
        if site_category in ['d41d8cd9','50e219e0']: 
            site_category = None
        if app_id in ['d41d8cd9','ecad2386']: 
            app_id = None
        if app_domain in ['d41d8cd9','7801e8d9']: 
            app_domain = None
        if app_category in ['d41d8cd9','07d7df22']: 
            app_category = None
        if device_id in ['d41d8cd9']: 
            device_id = None
        if device_ip in ['d41d8cd9']: 
            device_ip = None
        if device_model in ['d41d8cd9']: 
            device_model = None
        if device_type in ['d41d8cd9']: 
            device_type = None
        if device_conn_type in ['d41d8cd9']: 
            device_conn_type = None
        if C14 in ['d41d8cd9']: 
            C14 = None
        if C15 in ['d41d8cd9']: 
            C15 = None
        if C16 in ['d41d8cd9']: 
            C16 = None
        if C17 in ['d41d8cd9']: 
            C17 = None
        if C18 in ['d41d8cd9']: 
            C18 = None
        if C19 in ['d41d8cd9']: 
            C19 = None
        if C20 in ['d41d8cd9']: 
            C20 = None
        if C21 in ['d41d8cd9']: 
            C21 = None
            
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
