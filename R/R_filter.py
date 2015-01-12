# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 15:45:23 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

pred = 'ensemble/submission_ensemble.csv'               # path to training file

start = datetime.now()
with open('ensemble/submission_ensemble_filtered.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(pred))):
        ID = row['id']
        click = row['click']
        
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))