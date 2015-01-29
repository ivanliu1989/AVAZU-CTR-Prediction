# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 20:18:04 2015

@author: Ivan.Liuyanfeng
"""
import pandas as pd
import math

def zygmoid(x):
	#I know it's a common Sigmoid feature, but that's why I probably found
	#it on FastML too: https://github.com/zygmuntz/kaggle-stackoverflow/blob/master/sigmoid_mc.py
	return 1 / (1 + math.exp(-x))

with open("vw/submission_vw_name_1.csv","wb") as outfile:
	outfile.write("id,click\n")
	for line in open("vw/avazu.preds.app.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row[1],zygmoid(float(row[0]))))
	for line in open("vw/avazu.preds.site.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row[1],zygmoid(float(row[0]))))

'''
with open("avazu.preds.sparse.csv","wb") as outfile:
	outfile.write("id,click\n")
	for line in open("avazu.preds.app.sparse.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row,zygmoid(float(row[0]))))
	for line in open("avazu.preds.site.sparse.txt"):
		row = line.strip().split(" ")
		outfile.write("%s,%f\n"%(row,zygmoid(float(row[0]))))
  

submit_click = pd.read_csv("avazu.preds.sparse.csv",index_col = False)
submit_id = pd.read_csv("submission_vw_cubic2_0.3957190.csv",index_col = False) 

submit_click['id']=submit_id['id']

submit_click.to_csv("avazu.preds.sparse.csv",index = False)
'''