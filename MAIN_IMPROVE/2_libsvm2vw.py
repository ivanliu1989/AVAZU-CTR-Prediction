# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:21:02 2015

@author: ivan
"""
from csv import DictReader
from datetime import datetime

def libsvm_to_vw(loc_csv, loc_output):
  
  start = datetime.now()
  print("\nTurning %s into %s? %s"%(loc_csv,loc_output))
  
  with open(loc_output,"wb") as outfile:
      
    for line in open(loc_csv):
	try:
		y, x = line.split( " ", 1 )
	# ValueError: need more than 1 value to unpack
	except ValueError:
		print "line with ValueError (skipping):"
		print line
		continue
      
      if y in [0,'0']:
          y = '-1'
      new_line = y + " |i " + x
	outfile.write( new_line )
      
	  #Reporting progress
      if e % 100000 == 0:
        print("%s\t%s"%(e, str(datetime.now() - start)))

  print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))
    
