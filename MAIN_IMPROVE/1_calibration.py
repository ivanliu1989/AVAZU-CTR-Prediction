# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 12:04:57 2015

@author: ivan
"""
import pandas as pd
from csv import DictReader
from datetime import datetime

train_app_path = 'data/train_df_app_smooth_ex.csv'
test_app_path = 'data/test_df_app_smooth_ex.csv'
train_site_path = 'data/train_df_site_smooth_ex.csv'
test_site_path = 'data/test_df_site_smooth_ex.csv'

##-- app --##
train_app = pd.read_csv(train_app_path,index_col = False)
test_app = pd.read_csv(test_app_path,index_col = False)

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

len(app_id_train);len(app_id_test)
len(app_domain_train);len(app_domain_test)

##-- site --##
train_site = pd.read_csv(train_site_path,index_col = False)
test_site = pd.read_csv(test_site_path,index_col = False)

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