# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 10:22:58 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

train = 'data/train.csv'               # path to training file
test = 'data/test.csv' 

# -- test data -- #
"""
test_df = pd.read_csv(test)

test_df['dow'] = test_df['hour'].map(lambda x: str(x)[4:6])
test_df['hour'] = test_df['hour'].map(lambda x: str(x)[6:])  # 00-23
test_df['dow'] = 6                # 1,2,3,4,5,6,7
test_df['holiday'] = 1            # 1:yes 0:no 
test_df.head()
test_df['hour'].describe()

test_df.to_csv('data/test_df.csv',index=False)
test_df = pd.read_csv('data/test_df.csv')
del test_df['Unnamed: 0']
del test_df
"""

# -- train data -- #
# list(test_df.columns.values)

start = datetime.now()
with open('data/train_df.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21,dow\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        if row['hour'][4:6] in ['19','26']:
            dow = 1
        elif row['hour'][4:6] in ['20','27']:
            dow = 2
        elif row['hour'][4:6] in ['21','28']:
            dow = 3
        elif row['hour'][4:6] in ['22','29']:
            dow = 4
        elif row['hour'][4:6] in ['23','30']:
            dow = 5
        elif row['hour'][4:6] in ['18','25']:
            dow = 7
        elif row['hour'][4:6] in ['24','31']:
            dow = 6
        
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
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21),str(dow)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
        
 # -- test data -- #
start = datetime.now()
with open('data/test_df.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21,dow\n')
    for t, row in enumerate(DictReader(open(test))):
        # turn hour really into hour, it was originally YYMMDDHH
        if row['hour'][4:6] in ['19','26']:
            dow = 1
        elif row['hour'][4:6] in ['20','27']:
            dow = 2
        elif row['hour'][4:6] in ['21','28']:
            dow = 3
        elif row['hour'][4:6] in ['22','29']:
            dow = 4
        elif row['hour'][4:6] in ['23','30']:
            dow = 5
        elif row['hour'][4:6] in ['18','25']:
            dow = 7
        elif row['hour'][4:6] in ['24','31']:
            dow = 6
            
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
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21),str(dow)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
       
        
        
        
        
        
        
        
        
        
        
        
        