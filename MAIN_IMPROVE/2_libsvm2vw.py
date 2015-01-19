# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:21:02 2015

@author: ivan
"""
from csv import DictReader
from datetime import datetime

def libsvm_to_vw(loc_libsvm, loc_output):
    
    start = datetime.now()
    print("\nTurning %s into %s?"%(loc_libsvm,loc_output))
    
    with open(loc_output,"wb") as outfile:
        e = 0
        for line in open(loc_libsvm):
            e +=1
            try:
                y, x = line.split( " ", 1 )
            except ValueError:
                print "line with ValueError (skipping):"
                print line
                continue
            
            if y in [0,'0']:
                y = '-1'
            
            new_line = y + " |i " + x
            outfile.write( new_line )
            
            if e % 100000 == 0:
                print("%s\t%s"%(e, str(datetime.now() - start)))
    
    print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))
    


libsvm_to_vw("xgboost/data/libsvm_train_full_site.txt", "vw/sparse/train_df_site.vw")
libsvm_to_vw("xgboost/data/libsvm_test_site.txt", "vw/sparse/test_df_site.vw")
libsvm_to_vw("xgboost/data/libsvm_train_full_app.txt", "vw/sparse/train_df_app.vw")
libsvm_to_vw("xgboost/data/libsvm_test_app.txt", "vw/sparse/test_df_app.vw")
