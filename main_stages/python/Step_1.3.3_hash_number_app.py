# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 23:23:40 2015

@author: Ivan
"""
from datetime import datetime
from csv import DictReader

# A, paths
train = 'data/train_df_app_smooth.csv'               # path to training file
test = 'data/test_df_app_smooth.csv'                 # path to testing file
train_s = 'data/onehot/train_df_smooth_hash_app.csv'  # path of to be outputted submission file
test_s = 'data/onehot/test_df_smooth_hash_app.csv'  # path of to be outputted submission file
D = 2**39

start = datetime.now()
with open(train_s,"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        click = row['click']
        
        hour = row['hour']
        if hour != "":
            hour = abs(hash('hour' + str(hour))%D)
            
        C1 = row['C1']
        if C1 != "":
            C1 = abs(hash('C1' + str(C1))%D)
            
        banner_pos = row['banner_pos']
        if banner_pos != "":
            banner_pos = abs(hash('banner_pos' + str(banner_pos))%D)
            
        #site_id = row['site_id']
        #site_domain = row['site_domain']
        #site_category = row['site_category']
        app_id = row['app_id']
        if app_id != "":
            app_id = abs(hash('app_id' + str(app_id))%D)
            
        app_domain = row['app_domain']
        if app_domain != "":
            app_domain = abs(hash('app_domain' + str(app_domain))%D)
            
        app_category = row['app_category']
        if app_category != "":
            app_category = abs(hash('app_category' + str(app_category))%D)
            
        device_id = row['device_id']
        if device_id != "":
            device_id = abs(hash('device_id' + str(device_id))%D)
            
        device_ip = row['device_ip']
        if device_ip != "":
            device_ip = abs(hash('device_ip' + str(device_ip))%D)
            
        device_model = row['device_model']
        if device_model != "":
            device_model = abs(hash('device_model' + str(device_model))%D)
            
        device_type = row['device_type']
        if device_type != "":
            device_type = abs(hash('device_type' + str(device_type))%D)
            
        device_conn_type = row['device_conn_type']
        if device_conn_type != "":
            device_conn_type = abs(hash('device_conn_type' + str(device_conn_type))%D)
            
        C14 = row['C14']
        if C14 != "":
            C14 = abs(hash('C14' + str(C14))%D)
            
        C15 = row['C15']
        if C15 != "":
            C15 = abs(hash('C15' + str(C15))%D)
            
        C16 = row['C16']
        if C16 != "":
            C16 = abs(hash('C16' + str(C16))%D)
            
        C17 = row['C17']
        if C17 != "":
            C17 = abs(hash('C17' + str(C17))%D)
            
        C18 = row['C18']
        if C18 != "":
            C18 = abs(hash('C18' + str(C18))%D)
            
        C19 = row['C19']
        if C19 != "":
            C19 = abs(hash('C19' + str(C19))%D)
            
        C20 = row['C20']
        if C20 != "":
            C20 = abs(hash('C20' + str(C20))%D)
            
        C21 = row['C21']
        if C21 != "":
            C21 = abs(hash('C21' + str(C21))%D)
            

        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))


start = datetime.now()
with open(test_s,"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        
        hour = row['hour']
        if hour != "":
            hour = abs(hash('hour' + str(hour))%D)
            
        C1 = row['C1']
        if C1 != "":
            C1 = abs(hash('C1' + str(C1))%D)
            
        banner_pos = row['banner_pos']
        if banner_pos != "":
            banner_pos = abs(hash('banner_pos' + str(banner_pos))%D)
            
        #site_id = row['site_id']
        #site_domain = row['site_domain']
        #site_category = row['site_category']
        app_id = row['app_id']
        if app_id != "":
            app_id = abs(hash('app_id' + str(app_id))%D)
            
        app_domain = row['app_domain']
        if app_domain != "":
            app_domain = abs(hash('app_domain' + str(app_domain))%D)
            
        app_category = row['app_category']
        if app_category != "":
            app_category = abs(hash('app_category' + str(app_category))%D)
            
        device_id = row['device_id']
        if device_id != "":
            device_id = abs(hash('device_id' + str(device_id))%D)
            
        device_ip = row['device_ip']
        if device_ip != "":
            device_ip = abs(hash('device_ip' + str(device_ip))%D)
            
        device_model = row['device_model']
        if device_model != "":
            device_model = abs(hash('device_model' + str(device_model))%D)
            
        device_type = row['device_type']
        if device_type != "":
            device_type = abs(hash('device_type' + str(device_type))%D)
            
        device_conn_type = row['device_conn_type']
        if device_conn_type != "":
            device_conn_type = abs(hash('device_conn_type' + str(device_conn_type))%D)
            
        C14 = row['C14']
        if C14 != "":
            C14 = abs(hash('C14' + str(C14))%D)
            
        C15 = row['C15']
        if C15 != "":
            C15 = abs(hash('C15' + str(C15))%D)
            
        C16 = row['C16']
        if C16 != "":
            C16 = abs(hash('C16' + str(C16))%D)
            
        C17 = row['C17']
        if C17 != "":
            C17 = abs(hash('C17' + str(C17))%D)
            
        C18 = row['C18']
        if C18 != "":
            C18 = abs(hash('C18' + str(C18))%D)
            
        C19 = row['C19']
        if C19 != "":
            C19 = abs(hash('C19' + str(C19))%D)
            
        C20 = row['C20']
        if C20 != "":
            C20 = abs(hash('C20' + str(C20))%D)
            
        C21 = row['C21']
        if C21 != "":
            C21 = abs(hash('C21' + str(C21))%D)
            

        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))