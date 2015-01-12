# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 15:45:23 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

pred = 'data/submission_py_site_app_0.13_1_1_3_s5.csv'               # path to training file

start = datetime.now()
with open('data/submission_py_site_app_0.13_1_1_3_s5_filtered.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(pred))):
        ID = row['id']
        click = row['click']
        
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))