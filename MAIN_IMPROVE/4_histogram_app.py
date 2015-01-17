# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 22:35:35 2015

@author: Ivan.Liuyanfeng
"""
#((#nclick+ alpha *0.25)/(#ncount+alpha)) of CTR(alpha=10)
from datetime import datetime
from csv import DictReader
import pandas as pd

alpha = 10

train_site_path = 'data/train_df_site_smooth.csv'
test_site_path = 'data/test_df_site_smooth.csv'

train_site = pd.read_csv(train_site_path,index_col = False)
test_site = pd.read_csv(test_site_path,index_col = False)

train_site_hour = (train_site[['hour','click']].groupby('hour').sum()['click'] + alpha*0.25)/(train_site[['hour','click']].groupby('hour').count()['click']
 + 10)
train_site_C1 = (train_site[['C1','click']].groupby('C1').sum()['click'] + alpha*0.25)/(train_site[['C1','click']].groupby('C1').count()['click']
 + 10)
train_site_banner_pos=(train_site[['banner_pos','click']].groupby('banner_pos').sum()['click'] + alpha*0.25)/(train_site[['banner_pos','click']].groupby('banner_pos').count()['click']
 + 10)
train_site_site_id=(train_site[['site_id','click']].groupby('site_id').sum()['click'] + alpha*0.25)/(train_site[['site_id','click']].groupby('site_id').count()['click']
 + 10)
train_site_site_domain=(train_site[['site_domain','click']].groupby('site_domain').sum()['click'] + alpha*0.25)/(train_site[['site_domain','click']].groupby('site_domain').count()['click']
 + 10)
train_site_site_category=(train_site[['site_category','click']].groupby('site_category').sum()['click'] + alpha*0.25)/(train_site[['site_category','click']].groupby('site_category').count()['click']
 + 10)
train_site_device_id=(train_site[['device_id','click']].groupby('device_id').sum()['click'] + alpha*0.25)/(train_site[['device_id','click']].groupby('device_id').count()['click']
 + 10)
train_site_device_ip=(train_site[['device_ip','click']].groupby('device_ip').sum()['click'] + alpha*0.25)/(train_site[['device_ip','click']].groupby('device_ip').count()['click']
 + 10)
train_site_device_model=(train_site[['device_model','click']].groupby('device_model').sum()['click'] + alpha*0.25)/(train_site[['device_model','click']].groupby('device_model').count()['click']
 + 10)
train_site_device_type=(train_site[['device_type','click']].groupby('device_type').sum()['click'] + alpha*0.25)/(train_site[['device_type','click']].groupby('device_type').count()['click']
 + 10)
train_site_device_conn_type=(train_site[['device_conn_type','click']].groupby('device_conn_type').sum()['click'] + alpha*0.25)/(train_site[['device_conn_type','click']].groupby('device_conn_type').count()['click']
 + 10)
train_site_C14=(train_site[['C14','click']].groupby('C14').sum()['click'] + alpha*0.25)/(train_site[['C14','click']].groupby('C14').count()['click']
 + 10)
train_site_C15=(train_site[['C15','click']].groupby('C15').sum()['click'] + alpha*0.25)/(train_site[['C15','click']].groupby('C15').count()['click']
 + 10)
train_site_C16=(train_site[['C16','click']].groupby('C16').sum()['click'] + alpha*0.25)/(train_site[['C16','click']].groupby('C16').count()['click']
 + 10)
train_site_C17=(train_site[['C17','click']].groupby('C17').sum()['click'] + alpha*0.25)/(train_site[['C17','click']].groupby('C17').count()['click']
 + 10)
train_site_C18=(train_site[['C18','click']].groupby('C18').sum()['click'] + alpha*0.25)/(train_site[['C18','click']].groupby('C18').count()['click']
 + 10)
train_site_C19=(train_site[['C19','click']].groupby('C19').sum()['click'] + alpha*0.25)/(train_site[['C19','click']].groupby('C19').count()['click']
 + 10)
train_site_C20=(train_site[['C20','click']].groupby('C20').sum()['click'] + alpha*0.25)/(train_site[['C20','click']].groupby('C20').count()['click']
 + 10)
train_site_C21=(train_site[['C21','click']].groupby('C21').sum()['click'] + alpha*0.25)/(train_site[['C21','click']].groupby('C21').count()['click']
 + 10)

# -- train dataset -- #
input_file = 'data/train_df_site_smooth.csv'
output_file = 'data/histogram/train_histogram_site.csv'

start = datetime.now()
with open(output_file,"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,site_id,site_domain,site_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        ID = row['id']
        click = row['click']
        hour = row['hour']
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
        
        if int(hour) in train_site_hour: 
            hour = train_site_hour[int(hour)]
        else:
            hour = ((0+alpha*0.25)/(0+alpha))
            
        if int(C1) in train_site_C1: 
            C1 = train_site_C1[int(C1)]
        else:
            C1 = ((0+alpha*0.25)/(0+alpha))
            
        if int(banner_pos) in train_site_banner_pos: 
            banner_pos = train_site_banner_pos[int(banner_pos)]
        else:
            banner_pos = ((0+alpha*0.25)/(0+alpha))
            
        if str(site_id) in train_site_site_id: 
            site_id = train_site_site_id[str(site_id)]
        else:
            site_id = ((0+alpha*0.25)/(0+alpha))
            
        if str(site_domain) in train_site_site_domain: 
            site_domain = train_site_site_domain[str(site_domain)]
        else:
            site_domain = ((0+alpha*0.25)/(0+alpha))
            
        if str(site_category) in train_site_site_category: 
            site_category = train_site_site_category[str(site_category)]
        else:
            site_category = ((0+alpha*0.25)/(0+alpha))
            
        if str(device_id) in train_site_device_id: 
            device_id = train_site_device_id[str(device_id)]
        else:
            device_id = ((0+alpha*0.25)/(0+alpha))
            
        if str(device_ip) in train_site_device_ip: 
            device_ip = train_site_device_ip[str(device_ip)]
        else:
            device_ip = ((0+alpha*0.25)/(0+alpha))
            
        if str(device_model) in train_site_device_model: 
            device_model = train_site_device_model[str(device_model)]
        else:
            device_model = ((0+alpha*0.25)/(0+alpha))
            
        if int(device_type) in train_site_device_type: 
            device_type = train_site_device_type[int(device_type)]
        else:
            device_type = ((0+alpha*0.25)/(0+alpha))
            
        if int(device_conn_type) in train_site_device_conn_type: 
            device_conn_type = train_site_device_conn_type[int(device_conn_type)]
        else:
            device_conn_type = ((0+alpha*0.25)/(0+alpha))
            
        if int(C14) in train_site_C14: 
            C14 = train_site_C14[int(C14)]
        else:
            C14 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C15) in train_site_C15: 
            C15 = train_site_C15[int(C15)]
        else:
            C15 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C16) in train_site_C16: 
            C16 = train_site_C16[int(C16)]
        else:
            C16 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C17) in train_site_C17: 
            C17 = train_site_C17[int(C17)]
        else:
            C17 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C18) in train_site_C18: 
            C18 = train_site_C18[int(C18)]
        else:
            C18 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C19) in train_site_C19: 
            C19 = train_site_C19[int(C19)]
        else:
            C19 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C20) in train_site_C20: 
            C20 = train_site_C20[int(C20)]
        else:
            C20 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C21) in train_site_C21: 
            C21 = train_site_C21[int(C21)]
        else:
            C21 = ((0+alpha*0.25)/(0+alpha))
                    
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))


# -- test dataset -- #
input_file = 'data/test_df_site_smooth.csv'
output_file = 'data/histogram/test_histogram_site.csv'

start = datetime.now()
with open(output_file,"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,site_id,site_domain,site_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        ID = row['id']
        hour = row['hour']
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
        
        if int(hour) in train_site_hour: 
            hour = train_site_hour[int(hour)]
        else:
            hour = ((0+alpha*0.25)/(0+alpha))
            
        if int(C1) in train_site_C1: 
            C1 = train_site_C1[int(C1)]
        else:
            C1 = ((0+alpha*0.25)/(0+alpha))
            
        if int(banner_pos) in train_site_banner_pos: 
            banner_pos = train_site_banner_pos[int(banner_pos)]
        else:
            banner_pos = ((0+alpha*0.25)/(0+alpha))
            
        if str(site_id) in train_site_site_id: 
            site_id = train_site_site_id[str(site_id)]
        else:
            site_id = ((0+alpha*0.25)/(0+alpha))
            
        if str(site_domain) in train_site_site_domain: 
            site_domain = train_site_site_domain[str(site_domain)]
        else:
            site_domain = ((0+alpha*0.25)/(0+alpha))
            
        if str(site_category) in train_site_site_category: 
            site_category = train_site_site_category[str(site_category)]
        else:
            site_category = ((0+alpha*0.25)/(0+alpha))
            
        if str(device_id) in train_site_device_id: 
            device_id = train_site_device_id[str(device_id)]
        else:
            device_id = ((0+alpha*0.25)/(0+alpha))
            
        if str(device_ip) in train_site_device_ip: 
            device_ip = train_site_device_ip[str(device_ip)]
        else:
            device_ip = ((0+alpha*0.25)/(0+alpha))
            
        if str(device_model) in train_site_device_model: 
            device_model = train_site_device_model[str(device_model)]
        else:
            device_model = ((0+alpha*0.25)/(0+alpha))
            
        if int(device_type) in train_site_device_type: 
            device_type = train_site_device_type[int(device_type)]
        else:
            device_type = ((0+alpha*0.25)/(0+alpha))
            
        if int(device_conn_type) in train_site_device_conn_type: 
            device_conn_type = train_site_device_conn_type[int(device_conn_type)]
        else:
            device_conn_type = ((0+alpha*0.25)/(0+alpha))
            
        if int(C14) in train_site_C14: 
            C14 = train_site_C14[int(C14)]
        else:
            C14 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C15) in train_site_C15: 
            C15 = train_site_C15[int(C15)]
        else:
            C15 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C16) in train_site_C16: 
            C16 = train_site_C16[int(C16)]
        else:
            C16 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C17) in train_site_C17: 
            C17 = train_site_C17[int(C17)]
        else:
            C17 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C18) in train_site_C18: 
            C18 = train_site_C18[int(C18)]
        else:
            C18 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C19) in train_site_C19: 
            C19 = train_site_C19[int(C19)]
        else:
            C19 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C20) in train_site_C20: 
            C20 = train_site_C20[int(C20)]
        else:
            C20 = ((0+alpha*0.25)/(0+alpha))
        
        if int(C21) in train_site_C21: 
            C21 = train_site_C21[int(C21)]
        else:
            C21 = ((0+alpha*0.25)/(0+alpha))
                    
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(device_conn_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
