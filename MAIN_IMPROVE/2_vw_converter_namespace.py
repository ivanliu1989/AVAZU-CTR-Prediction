# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 09:36:23 2015

@author: Ivan.Liuyanfeng
"""
from csv import DictReader
from datetime import datetime

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
           categorical_features += "|%s %s " % (str(k),str(v))
			  
	  #Creating the labels		  
      if train: #we care about labels
        if row['click'] == '1':
          label = 1
        else:
          label = -1 #we set negative label to -1
        outfile.write( "%s '%s %s\n" % (label,row['id'],categorical_features) )
		
      else: #we dont care about labels
        outfile.write( "1 '%s %s\n" % (row['id'],categorical_features) )
      
	  #Reporting progress
      if e % 100000 == 0:
        print("%s\t%s"%(e, str(datetime.now() - start)))

  print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))


csv_to_vw("data/train_df_site_smooth.csv", "vw/train_df_site.vw",train=True)
csv_to_vw("data/test_df_site_smooth.csv", "vw/test_df_site.vw",train=False)
csv_to_vw("data/train_df_app_smooth.csv", "vw/train_df_app.vw",train=True)
csv_to_vw("data/test_df_app_smooth.csv", "vw/test_df_app.vw",train=False)