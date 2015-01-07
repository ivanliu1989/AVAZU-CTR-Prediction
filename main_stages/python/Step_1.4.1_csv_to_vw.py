# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 13:36:16 2015

@author: ivan
"""

from datetime import datetime
from csv import DictReader

def csv_to_vw(loc_csv, loc_output, train=True):
  
  start = datetime.now()
  print("\nTurning %s into %s. Is_train_set? %s"%(loc_csv,loc_output,train))
  
  with open(loc_output,"wb") as outfile:
    for e, row in enumerate(DictReader(open(loc_csv))):
	
	  #Creating the features
      numerical_features = ""
      categorical_features = ""
      for k,v in row.items():
        if k not in ["id","click"]:
          if len(str(v)) > 0:
           categorical_features += " %s" % v
			  
	  #Creating the labels		  
      if train: #we care about labels
        if row['click'] == '1':
          label = 1
        else:
          label = -1 #we set negative label to -1
        outfile.write( "%s '%s |i%s |c%s\n" % (label,row['id'],numerical_features,categorical_features) )
		
      else: #we dont care about labels
        outfile.write( "1 '%s |i%s |c%s\n" % (row['id'],numerical_features,categorical_features) )
      
	  #Reporting progress
      if e % 100000 == 0:
        print("%s\t%s"%(e, str(datetime.now() - start)))

  print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))


csv_to_vw("data/train_df.csv", "vw/train_df.vw",train=True)
csv_to_vw("data/test_df.csv", "vw/test_df.vw",train=False)
