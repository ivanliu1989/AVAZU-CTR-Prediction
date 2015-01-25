# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 13:44:10 2015

@author: Ivan
"""
from datetime import datetime
from csv import DictReader

###############################
# --- Main transformation --- #
###############################
input_file = 'data/train_df_app_smooth.csv'
output_file_0 = 'data/train_df_app_smooth_conn_0.csv'
output_file_2 = 'data/train_df_app_smooth_conn_2.csv'
output_file_3 = 'data/train_df_app_smooth_conn_3.csv'
output_file_5 = 'data/train_df_app_smooth_conn_5.csv'

start = datetime.now()
with open(output_file_0,"wb") as outfile:
    outfile.write('id,click,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 0:
            
            ID = row['id']
            click = row['click']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))

start = datetime.now()
with open(output_file_2,"wb") as outfile:
    outfile.write('id,click,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 2:
            
            ID = row['id']
            click = row['click']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
   
start = datetime.now()
with open(output_file_3,"wb") as outfile:
    outfile.write('id,click,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 3:
            
            ID = row['id']
            click = row['click']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
                
start = datetime.now()
with open(output_file_5,"wb") as outfile:
    outfile.write('id,click,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 5:
            
            ID = row['id']
            click = row['click']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
         
####################################
# --- Main transformation test --- #
####################################
input_file = 'data/test_df_app_smooth.csv'
output_file_0 = 'data/test_df_app_smooth_conn_0.csv'
output_file_2 = 'data/test_df_app_smooth_conn_2.csv'
output_file_3 = 'data/test_df_app_smooth_conn_3.csv'
output_file_5 = 'data/test_df_app_smooth_conn_5.csv'

start = datetime.now()
with open(output_file_0,"wb") as outfile:
    outfile.write('id,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 0:
            
            ID = row['id']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))

start = datetime.now()
with open(output_file_2,"wb") as outfile:
    outfile.write('id,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 2:
            
            ID = row['id']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
                
start = datetime.now()
with open(output_file_3,"wb") as outfile:
    outfile.write('id,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 3:
            
            ID = row['id']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
                
start = datetime.now()
with open(output_file_5,"wb") as outfile:
    outfile.write('id,hour,dow,C1,banner_pos,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,C14,C15,C16,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(input_file))):
        
        if int(row['device_conn_type']) == 5:
            
            ID = row['id']
            hour = row['hour']
            dow=row['dow']
            C1 = row['C1']
            banner_pos = row['banner_pos']
            app_id = row['app_id']
            app_domain = row['app_domain']
            app_category = row['app_category']
            device_id = row['device_id']
            device_ip = row['device_ip']
            device_model = row['device_model']
            device_type = row['device_type']
            C14 = row['C14']
            C15 = row['C15']
            C16 = row['C16']
            C17 = row['C17']
            C18 = row['C18']
            C19 = row['C19']
            C20 = row['C20']
            C21 = row['C21']
            
            outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(dow),str(C1),str(banner_pos),str(app_id),str(app_domain),str(app_category),str(device_id),str(device_ip),str(device_model),str(device_type),str(C14),str(C15),str(C16),str(C17),str(C18),str(C19),str(C20),str(C21)))
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))

