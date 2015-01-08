# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:46:43 2015

@author: ivan
"""
from datetime import datetime
from csv import DictReader

###############################
# --- Main transformation --- #
###############################
input_file = 'data/train_df_n.csv'
output_file = 'xgboost/libsvm_train_n.txt'
D = 2**28  #10**6 

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
        
        j = 0

        for i, item in row.items():
            
            index = abs(hash(i + '_' + item)%D)
                
            j += 1
            
            # print(i + ': ' + item + ': ' + str(index))
            
            if index == '' or float(index) == 0.0:
                continue
            
            new_item = "%s:%s" % ( j-1, index )
            new_line.append( new_item )
            
        
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
        
        # print(new_line)
            
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            
####################################
# --- Main transformation test --- #
####################################
input_file = 'data/test_df_n.csv'
output_file = 'xgboost/libsvm_test_n.txt'
D = 2**28  #10**6 

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
    
        label = '0'
        
        new_line.append(label)
        
        del row['id']
        
        j = 0
        
        for i, item in row.items():
            
            index = abs(hash(i + '_' + item)%D)
                
            j += 1
            
            if index == '' or float(index) == 0.0:
                continue
            
            new_item = "%s:%s" % ( j-1, index )
            new_line.append( new_item )
            
        
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
        
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))

   
