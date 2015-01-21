# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:35:42 2015

@author: ivan
"""

with open("vw/submission_vw_name_logistic.csv","wb") as outfile:
	outfile.write("id,click\n")
	for line in open("vw/logistic/avazu.preds.app.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row[1],float(row[0])))
	for line in open("vw/logistic/avazu.preds.site.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row[1],float(row[0])))
