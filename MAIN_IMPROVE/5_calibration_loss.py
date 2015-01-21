# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 20:26:08 2015

@author: Ivan.Liuyanfeng
"""
from csv import DictReader
from datetime import datetime

submit_path = 'Blending_models_BM_CU_FM_XG_NN.csv'

start = datetime.now()
with open('Blending_models_BM_CU_FM_XG_NN_calLoss.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(submit_path))):
        
        ID = row['id']
        click = row['click']
        if float(click) > .99:
            click = 0.999999
        elif float(click) < 0.01:
            click = 0.000001
        else:
            click = float(click)
            
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        
        if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
         