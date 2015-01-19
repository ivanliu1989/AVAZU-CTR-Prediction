# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:30:04 2015

@author: ivan
"""

import math

def zygmoid(x):
	#I know it's a common Sigmoid feature, but that's why I probably found
	#it on FastML too: https://github.com/zygmuntz/kaggle-stackoverflow/blob/master/sigmoid_mc.py
	return 1 / (1 + math.exp(-x))

with open("vw/submission_vw_name_l4.5.csv","wb") as outfile:
	outfile.write("id,click\n")
	for line in open("vw/avazu.preds.app.name.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row[1],zygmoid(float(row[0]))))
	for line in open("vw/avazu.preds.site.name.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row[1],zygmoid(float(row[0]))))
