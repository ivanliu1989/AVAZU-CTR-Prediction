# -*- coding: UTF-8 -*-

########################################################
# __Author__: Xueer Chen <snowwing922@gmail.com>             #
# Kaggle competition "Display Advertising Challenge":  #
# https://www.kaggle.com/c/avazu-ctr-prediction #
# Credit: Triskelion <info@mlwave.com>            #
########################################################

from datetime import datetime
from csv import DictReader

def csv_to_vw(loc_csv, loc_output, train=True):
  """
  Munges a CSV file (loc_csv) to a VW file (loc_output). Set "train"
  to False when munging a test set.
  TODO: Too slow for a daily cron job. Try optimize, Pandas or Go.
  """
  start = datetime.now()
  print("\nTurning %s into %s. Is_train_set? %s"%(loc_csv,loc_output,train))
  
  with open(loc_output,"wb") as outfile:
    for e, row in enumerate( DictReader(open(loc_csv)) ):
	
	  #Creating the features
      numerical_features = ""
      categorical_features = ""
      for k,v in row.items():
        if k not in ["id","click"]:
          if len(str(v)) > 0:
           categorical_features += " %s" % v
			  
	  #Creating the labels		  
      if train: #we care about labels
        if row['click'] == "1":
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

csv_to_vw("train.csv", "train.vw",train=True)
csv_to_vw("test.csv", "test.vw",train=False)
