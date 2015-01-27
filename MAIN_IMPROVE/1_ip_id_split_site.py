# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 10:52:53 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

train = 'other/train_df_site.csv'               # path to training file
test = 'other/test_df_site.csv' 

# -- train data -- #
# list(test_df.columns.values)

start = datetime.now()
with open('other/train_df_site_split.csv',"wb") as outfile:
    outfile.write('id,click,hour,C1,banner_pos,site_id,site_domain,site_domain_hf,site_category,device_id,device_ip,device_id_2,device_ip_2,device_model,device_type,device_conn_type,C14,img_size,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(train))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        click = row['click']
        hour = row['hour']

        C1 = row['C1']
        if (C1 in ['']):
            C1 = '1005'

        banner_pos = row['banner_pos']
        if (banner_pos in ['']):
            banner_pos = '0'

        site_id = row['site_id']
        if (site_id in ['']):
            site_id = '1fbe01fe'

        site_domain = row['site_domain']
        if (site_domain in ['']):
            site_domain = 'f3845767'
        site_domain_hf = site_domain[0:2] + site_domain[6:8]

        site_category = row['site_category']
        if (site_category in ['']):
            site_category = 'f028772b'

        device_id = row['device_id']
        if (device_id in ['']):
            device_id = 'a99f214a'

        device_ip = row['device_ip']
        if (device_ip in ['']):
            device_ip = '6b9769f2'

        device_id_2 = row['device_id'][0:4]
        device_ip_2 = row['device_ip'][0:4]

        device_model = row['device_model']
        if (device_model in ['']):
            device_model = '8a4875bd'

        device_type = row['device_type']
        if (device_type in ['']):
            device_type = '1'

        device_conn_type = row['device_conn_type']
        if (device_conn_type in ['']):
            device_conn_type = '0'

        C14 = row['C14']
        if (C14 in ['']):
            C14 = '19771'

        img_size = row['C15'] + '*' + row['C16']
        if (img_size in ['320*480', '480*320']):
            img_size = '480*320'
        if (img_size in ['768*1024', '1024*768']):
            img_size = '1024*768'

        C17 = row['C17']
        if (C17 in ['']):
            C17 = '1722'

        C18 = row['C18']
        if (C18 in ['']):
            C18 = '0'

        C19 = row['C19']
        if (C19 in ['']):
            C19 = '35'

        C20 = row['C20']
        if (C20 in ['']):
            C20 = '-1'

        C21 = row['C21']
        if (C21 in ['']):
            C21 = '23'
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID), str(click),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_domain_hf),str(site_category),str(device_id),str(device_ip),str(device_id_2),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(img_size),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
        
 # -- test data -- #
start = datetime.now()
with open('other/test_df_site_split.csv',"wb") as outfile:
    outfile.write('id,hour,C1,banner_pos,site_id,site_domain,site_domain_hf,site_category,device_id,device_ip,device_id_2,device_ip_2,device_model,device_type,device_conn_type,C14,img_size,C17,C18,C19,C20,C21\n')
    for t, row in enumerate(DictReader(open(test))):
        # turn hour really into hour, it was originally YYMMDDHH
        
        ID = row['id']
        hour = row['hour']
        
        C1 = row['C1']
        if (C1 in ['']):
            C1 = '1005'

        banner_pos = row['banner_pos']
        if (banner_pos in ['']):
            banner_pos = '0'

        site_id = row['site_id']
        if (site_id in ['']):
            site_id = '1fbe01fe'

        site_domain = row['site_domain']
        if (site_domain in ['']):
            site_domain = 'f3845767'
        site_domain_hf = site_domain[0:2] + site_domain[6:8]
            
        site_category = row['site_category']
        if (site_category in ['']):
            site_category = 'f028772b'

        device_id = row['device_id']
        if (device_id in ['']):
            device_id = 'a99f214a'

        device_ip = row['device_ip']
        if (device_ip in ['']):
            device_ip = '6b9769f2'

        device_id_2 = row['device_id'][0:4]
        device_ip_2 = row['device_ip'][0:4]

        device_model = row['device_model']
        if (device_model in ['']):
            device_model = '8a4875bd'

        device_type = row['device_type']
        if (device_type in ['']):
            device_type = '1'

        device_conn_type = row['device_conn_type']
        if (device_conn_type in ['']):
            device_conn_type = '0'

        C14 = row['C14']
        if (C14 in ['']):
            C14 = '19771'

        img_size = row['C15'] + '*' + row['C16']
        if (img_size in ['320*480', '480*320']):
            img_size = '480*320'
        if (img_size in ['768*1024', '1024*768']):
            img_size = '1024*768'

        C17 = row['C17']
        if (C17 in ['']):
            C17 = '1722'

        C18 = row['C18']
        if (C18 in ['']):
            C18 = '0'

        C19 = row['C19']
        if (C19 in ['']):
            C19 = '35'

        C20 = row['C20']
        if (C20 in ['']):
            C20 = '-1'

        C21 = row['C21']
        if (C21 in ['']):
            C21 = '23'
        
        
        outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (str(ID),str(hour),str(C1),str(banner_pos),str(site_id),str(site_domain),str(site_domain_hf),str(site_category),str(device_id),str(device_ip),str(device_id_2),str(device_ip_2),str(device_model),str(device_type),str(device_conn_type),str(C14),str(img_size),str(C17),str(C18),str(C19),str(C20),str(C21)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        
