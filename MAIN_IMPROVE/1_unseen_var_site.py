# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 11:00:37 2015

@author: ivan
"""
import pandas as pd
from csv import DictReader
from datetime import datetime

train_site_path = 'data/train_df_site_smooth.csv'
test_site_path = 'data/test_df_site_smooth.csv'

train_site = pd.read_csv(train_site_path,index_col = False)
test_site = pd.read_csv(test_site_path,index_col = False)

#site_col = list(train_site.columns.values)
#del site_col[0];del site_col[0];del site_col[0];del site_col[0];del site_col[0]
#del site_col[7];del site_col[11];del site_col[11];del site_col[12]
# hour, c1, banner, device_conn_type, C18, C19, C21
site_id_train = set(train_site['site_id'])
site_domain_train = set(train_site['site_domain'])
site_category_train = set(train_site['site_category'])
device_id_train = set(train_site['device_id'])
device_ip_train = set(train_site['device_ip'])
device_model_train = set(train_site['device_model'])
device_type_train = set(train_site['device_type'])
C14_train = set(train_site['C14'])
C15_train = set(train_site['C15'])
C16_train = set(train_site['C16'])
C17_train = set(train_site['C17'])
C20_train = set(train_site['C20'])

site_id_test = set(test_site['site_id'])
site_domain_test = set(test_site['site_domain'])
site_category_test = set(test_site['site_category'])
device_id_test = set(test_site['device_id'])
device_ip_test = set(test_site['device_ip'])
device_model_test = set(test_site['device_model'])
device_type_test = set(test_site['device_type']) #int
C14_test = set(test_site['C14']) #int
C15_test = set(test_site['C15']) #int
C16_test = set(test_site['C16']) #int
C17_test = set(test_site['C17']) #int
C20_test = set(test_site['C20']) #int

del train_site; del test_site

##-- test --##
start = datetime.now()
with open('data/test_df_site_smooth_ex.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,site_id,site_domain,site_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test_site_path))):
        
        ID = row['id']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']
        site_id = row['site_id'] #
        site_domain = row['site_domain'] #
        site_category = row['site_category'] #
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
        
        if str(site_id) not in site_id_train and str(site_id) != '':
            site_id = ''
        if str(site_domain) not in site_domain_train and str(site_domain) != '':
            site_domain = ''
        if str(site_category) not in site_category_train and str(site_category) != '':
            site_category = ''
        if str(device_id) not in device_id_train and str(device_id) != '':
            device_id = ''
        if str(device_ip) not in device_ip_train and str(device_ip) != '':
            device_ip = ''
        if str(device_model) not in device_model_train and str(device_model) != '':
            device_model = ''
        if int(device_type) not in device_type_train and int(device_type) != '':
            device_type = ''
        if int(C14) not in C14_train and int(C14) != '':
            C14 = ''
        if int(C15) not in C15_train and int(C15) != '':
            C15 = ''
        if int(C16) not in C16_train and int(C16) != '':
            C16 = ''
        if int(C17) not in C17_train and int(C17) != '':
            C17 = ''
        if int(C20) not in C20_train and int(C20) != '':
            C20 = ''
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
##-- train --##
start = datetime.now()
with open('data/train_df_site_smooth_ex.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,site_id,site_domain,site_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train_site_path))):
        
        ID = row['id']
        click = row['click']
        hour = row['hour']
        C1 = row['C1']
        banner_pos = row['banner_pos']
        site_id = row['site_id'] #
        site_domain = row['site_domain'] #
        site_category = row['site_category'] #
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
        
        if str(site_id) not in site_id_test and str(site_id) != '':
            site_id = ''
        if str(site_domain) not in site_domain_test and str(site_domain) != '':
            site_domain = ''
        if str(site_category) not in site_category_test and str(site_category) != '':
            site_category = ''
        if str(device_id) not in device_id_test and str(device_id) != '':
            device_id = ''
        if str(device_ip) not in device_ip_test and str(device_ip) != '':
            device_ip = ''
        if str(device_model) not in device_model_test and str(device_model) != '':
            device_model = ''
        if int(device_type) not in device_type_test and int(device_type) != '':
            device_type = ''
        if int(C14) not in C14_test and int(C14) != '':
            C14 = ''
        if int(C15) not in C15_test and int(C15) != '':
            C15 = ''
        if int(C16) not in C16_test and int(C16) != '':
            C16 = ''
        if int(C17) not in C17_test and int(C17) != '':
            C17 = ''
        if int(C20) not in C20_test and int(C20) != '':
            C20 = ''
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(click),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))