# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 10:55:01 2015

@author: Ivan.Liuyanfeng
"""
from datetime import datetime
from csv import DictReader

###############################
# --- Main transformation --- #
###############################
input_file = 'data/histogram/train_histogram_app.csv'
output_file = 'xgboost/libsvm_train_app_hist.txt'

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
    
        if row['click'] == '0':
            label = '0'
        elif row['click'] == '1':
            label = '1'
        else:
            break
        
        new_line.append(label)
        
        del row['id']
        del row['click']
        
        index = 0
        for i, item in row.items():
            
            index += 1
            
            if item in ['',0,'0']:
                continue
              
            new_item = "%s:%s" % ( index-1, item )
            new_line.append( new_item )
            
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
 
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))


input_file = 'data/histogram/train_histogram_site.csv'
output_file = 'xgboost/libsvm_train_site_hist.txt'

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
    
        if row['click'] == '0':
            label = '0'
        elif row['click'] == '1':
            label = '1'
        else:
            break
        
        new_line.append(label)
        
        del row['id']
        del row['click']
        
        index = 0
        for i, item in row.items():
            
            index += 1
            
            if item in ['',0,'0']:
                continue
              
            new_item = "%s:%s" % ( index-1, item )
            new_line.append( new_item )
            
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
 
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
             
####################################
# --- Main transformation test --- #
####################################

input_file = 'data/histogram/test_histogram_app.csv'
output_file = 'xgboost/libsvm_test_app_hist.txt'

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
    
        label = '0'
        
        new_line.append(label)
        
        del row['id']
        
        index = 0
        for i, item in row.items():
            
            index += 1
            
            if item in ['',0,'0']:
                continue
              
            new_item = "%s:%s" % ( index-1, item )
            new_line.append( new_item )
            
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
 
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
             

input_file = 'data/histogram/test_histogram_site.csv'
output_file = 'xgboost/libsvm_test_site_hist.txt'

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
    
        label = '0'
        
        new_line.append(label)
        
        del row['id']
        
        index = 0
        for i, item in row.items():
            
            index += 1
            
            if item in ['',0,'0']:
                continue
              
            new_item = "%s:%s" % ( index-1, item )
            new_line.append( new_item )
            
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
 
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
        