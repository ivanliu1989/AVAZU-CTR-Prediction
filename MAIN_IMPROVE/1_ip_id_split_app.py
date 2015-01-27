# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 10:52:53 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

train = 'other/train_df_app.csv'               # path to training file
test = 'other/test_df_app.csv' 

# -- train data -- #
# list(test_df.columns.values)

start = datetime.now()
with open('other/train_df_app_split.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,app_id,app_domain,app_category,device_id_1,device_id_2,device_ip_1,device_ip_2,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        click = row['click']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']
        app_id = row['app_id']
        app_domain = row['app_domain']
        app_category = row['app_category']
        device_id_1 = row['device_id'][0:4]
        device_ip_1 = row['device_ip'][0:4]
        device_id_2 = row['device_id'][4:]
        device_ip_2 = row['device_ip'][4:]
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
        
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id_1),str(device_id_2),str(device_ip_1),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
        
 # -- test data -- #
start = datetime.now()
with open('other/test_df_app_split.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,app_id,app_domain,app_category,device_id_1,device_id_2,device_ip_1,device_ip_2,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']
        app_id = row['app_id']
        app_domain = row['app_domain']
        app_category = row['app_category']
        device_id_1 = row['device_id'][0:4]
        device_ip_1 = row['device_ip'][0:4]
        device_id_2 = row['device_id'][4:]
        device_ip_2 = row['device_ip'][4:]
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
        
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id_1),str(device_id_2),str(device_ip_1),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
