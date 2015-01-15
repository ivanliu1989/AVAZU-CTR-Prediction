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
input_file = 'data/onehot/train_df_smooth_hash_app.csv'
output_file = 'sofia-ml/data/sofia_train_app.txt'
var_dict = {}
for t, row in enumerate(DictReader(open("data/onehot/app_var_dict.csv"))): # site/app
    var_dict[row['key']] = row['val']

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
        new_item = []
        
        if row['click'] == '0':
            label = '0'
        elif row['click'] == '1':
            label = '1'
        else:
            break
        
        new_line.append(label)
        
        del row['id']
        del row['click']

        for i, item in row.items():

            if item in ['',0,'0']:
                continue
            
            index = int(var_dict[str(item)+'.0']) + 1           
              
            # print(i + ': ' + item + ': ' + str(index))
            
            new_item.append(index)
            
        new_item = sorted(new_item)
        
        for index in new_item:
            
            item = "%s:%s" % ( index, 1 )
            new_line.append( item )
        
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
        
        # print(new_line)
            
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))


input_file = 'data/onehot/train_df_smooth_hash_site.csv'
output_file = 'sofia-ml/data/sofia_train_site.txt'
var_dict = {}
for t, row in enumerate(DictReader(open("data/onehot/site_var_dict.csv"))): # site/app
    var_dict[row['key']] = row['val']

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
        new_item = []
        if row['click'] == '0':
            label = '0'
        elif row['click'] == '1':
            label = '1'
        else:
            break
        
        new_line.append(label)
        
        del row['id']
        del row['click']

        for i, item in row.items():

            if item in ['',0,'0']:
                continue
            
            index = int(var_dict[str(item)+'.0']) + 1           
              
            # print(i + ': ' + item + ': ' + str(index))
            
            new_item.append(index)
            
        new_item = sorted(new_item)
        
        for index in new_item:
            
            item = "%s:%s" % ( index, 1 )
            new_line.append( item )
        
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
        
        # print(new_line)
            
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
             
####################################
# --- Main transformation test --- #
####################################
input_file = 'data/onehot/test_df_smooth_hash_app.csv'
output_file = 'sofia-ml/data/sofia_test_app.txt'
var_dict = {}
for t, row in enumerate(DictReader(open("data/onehot/app_var_dict.csv"))): # site/app
    var_dict[row['key']] = row['val']

start = datetime.now()
ex_f = 0 
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
        new_item = []
        label = '0'
        
        new_line.append(label)
        
        del row['id']
        
        for i, item in row.items():

            if item in ['',0,'0']:
                continue
            
            if str(item)+'.0' in var_dict:
                index = int(var_dict[str(item)+'.0']) + 1 
                new_item.append(index)
            else:
                ex_f += 1
                continue
              
            # print(i + ': ' + item + ': ' + str(index))
            
        new_item = sorted(new_item)
        
        for index in new_item:
            
            item = "%s:%s" % ( index, 1 )
            new_line.append( item )
            
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
        
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            print(ex_f)


input_file = 'data/onehot/test_df_smooth_hash_site.csv'
output_file = 'sofia-ml/data/sofia_test_site.txt'
var_dict = {}
for t, row in enumerate(DictReader(open("data/onehot/site_var_dict.csv"))): # site/app
    var_dict[row['key']] = row['val']

start = datetime.now()
ex_f = 0 
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        new_line = []
        new_item = []
        label = '0'
        
        new_line.append(label)
        
        del row['id']
        
        for i, item in row.items():

            if item in ['',0,'0']:
                continue
            
            if str(item)+'.0' in var_dict:
                index = int(var_dict[str(item)+'.0']) + 1 
                new_item.append(index)
            else:
                ex_f += 1
                continue
              
            # print(i + ': ' + item + ': ' + str(index))
            
        new_item = sorted(new_item)
        
        for index in new_item:
            
            item_n = "%s:%s" % ( index, 1 )
            new_line.append( item_n )
            
        new_line = " ".join( new_line )        
        new_line += "\n"            
        outfile.write(new_line)
        
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))
            print(ex_f)
 
