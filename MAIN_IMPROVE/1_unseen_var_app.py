# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 11:00:37 2015

@author: ivan
"""
import pandas as pd
from csv import DictReader
from datetime import datetime

train_app_path = 'data/train_df_app_smooth.csv'
test_app_path = 'data/test_df_app_smooth.csv'

train_app = pd.read_csv(train_app_path,index_col = False)
test_app = pd.read_csv(test_app_path,index_col = False)

#app_col = list(train_app.columns.values)
#del app_col[0];del app_col[0];del app_col[0];del app_col[0];del app_col[0]
#del app_col[7];del app_col[11];del app_col[11];del app_col[12]
# hour, c1, banner, device_conn_type, C18, C19, C21
app_id_train = set(train_app['app_id'])
app_domain_train = set(train_app['app_domain'])
app_category_train = set(train_app['app_category'])
device_id_train = set(train_app['device_id'])
device_ip_train = set(train_app['device_ip'])
device_model_train = set(train_app['device_model'])
device_type_train = set(train_app['device_type'])
C14_train = set(train_app['C14'])
C15_train = set(train_app['C15'])
C16_train = set(train_app['C16'])
C17_train = set(train_app['C17'])
C20_train = set(train_app['C20'])

app_id_test = set(test_app['app_id'])
app_domain_test = set(test_app['app_domain'])
app_category_test = set(test_app['app_category'])
device_id_test = set(test_app['device_id'])
device_ip_test = set(test_app['device_ip'])
device_model_test = set(test_app['device_model'])
device_type_test = set(test_app['device_type']) #int
C14_test = set(test_app['C14']) #int
C15_test = set(test_app['C15']) #int
C16_test = set(test_app['C16']) #int
C17_test = set(test_app['C17']) #int
C20_test = set(test_app['C20']) #int

del train_app; del test_app

##-- test --##
start = datetime.now()
with open('data/test_df_app_smooth_ex.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test_app_path))):
        
        ID = row['id']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']
        app_id = row['app_id'] #
        app_domain = row['app_domain'] #
        app_category = row['app_category'] #
        device_id = row['device_id'] #
        device_ip = row['device_ip'] #
        device_model = row['device_model'] #
        device_type = row['device_type'] #
        device_conn_type = row['device_conn_type']
        C14 = row['C14'] #
        C15 = row['C15'] #
        C16 = row['C16'] #
        C17 = row['C17'] #
        C18 = row['C18']
        C19 = row['C19']
        C20 = row['C20'] #
        C21 = row['C21']
        
        if str(app_id) not in app_id_train and str(app_id) != '':
            app_id = -2
        if str(app_domain) not in app_domain_train and str(app_domain) != '':
            app_domain = -2
        if str(app_category) not in app_category_train and str(app_category) != '':
            app_category = -2
        if str(device_id) not in device_id_train and str(device_id) != '':
            device_id = -2
        if str(device_ip) not in device_ip_train and str(device_ip) != '':
            device_ip = -2
        if str(device_model) not in device_model_train and str(device_model) != '':
            device_model = -2
        if int(device_type) not in device_type_train and int(device_type) != '':
            device_type = -2
        if int(C14) not in C14_train and int(C14) != '':
            C14 = -2
        if int(C15) not in C15_train and int(C15) != '':
            C15 = -2
        if int(C16) not in C16_train and int(C16) != '':
            C16 = -2
        if int(C17) not in C17_train and int(C17) != '':
            C17 = -2
        if int(C20) not in C20_train and int(C20) != '':
            C20 = -2
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
##-- train --##
start = datetime.now()
with open('data/train_df_app_smooth_ex.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train_app_path))):
        
        ID = row['id']
        click = row['click']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']
        app_id = row['app_id'] #
        app_domain = row['app_domain'] #
        app_category = row['app_category'] #
        device_id = row['device_id'] #
        device_ip = row['device_ip'] #
        device_model = row['device_model'] #
        device_type = row['device_type'] #
        device_conn_type = row['device_conn_type']
        C14 = row['C14'] #
        C15 = row['C15'] #
        C16 = row['C16'] #
        C17 = row['C17'] #
        C18 = row['C18']
        C19 = row['C19']
        C20 = row['C20'] #
        C21 = row['C21']
        
        if str(app_id) not in app_id_test and str(app_id) != '':
            app_id = -2
        if str(app_domain) not in app_domain_test and str(app_domain) != '':
            app_domain = -2
        if str(app_category) not in app_category_test and str(app_category) != '':
            app_category = -2
        if str(device_id) not in device_id_test and str(device_id) != '':
            device_id = -2
        if str(device_ip) not in device_ip_test and str(device_ip) != '':
            device_ip = -2
        if str(device_model) not in device_model_test and str(device_model) != '':
            device_model = -2
        if int(device_type) not in device_type_test and int(device_type) != '':
            device_type = -2
        if int(C14) not in C14_test and int(C14) != '':
            C14 = -2
        if int(C15) not in C15_test and int(C15) != '':
            C15 = -2
        if int(C16) not in C16_test and int(C16) != '':
            C16 = -2
        if int(C17) not in C17_test and int(C17) != '':
            C17 = -2
        if int(C20) not in C20_test and int(C20) != '':
            C20 = -2
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(click),str(hour),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))