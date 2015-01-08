# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 22:54:48 2015

@author: Ivan
"""
import pandas as pd
from collections import Counter
import os
import numpy as np

train = 'data/train_df_app.csv'               # path to training file
test = 'data/test_df_app.csv'
#train = 'data/train_df_site.csv'               # path to training file
#test = 'data/test_df_site.csv'
test_df = pd.read_csv(test)
train_df = pd.read_csv(train)

create_dict_for = ["C1","C4","banner_pos","site_id","site_domain","site_category",
                   "app_id","app_domain","app_category","device_id","device_ip",
                   "device_model"]

COLS = list(train_df.columns.values)

CHUNK_SIZE = 1000000

def create_counters():    
    counters = {}
    for col in create_dict_for:
        counters[col] = Counter()
    return counters
    
def update_counter(path,counters):
    df = pd.read_csv(path,chunksize=CHUNK_SIZE,iterator=True)
    for chunk in df:    
        for col in create_dict_for:
            counters[col].update(chunk.ix[:,col])

def convert_counts_to_id(counters):
    ids = {}
    for col in create_dict_for:
        ids[col] = {}
        for i,(val,_) in enumerate(counters[col].most_common()):
            ids[col][val] = i
    return ids
    
def write_translated(input_path,output_path,ids,mode="w",start_id=0):
    df = pd.read_csv(input_path,chunksize=CHUNK_SIZE,iterator=True)
    for i, chunk in enumerate(df):
        for col in create_dict_for:
            chunk.ix[:,col] = chunk.ix[:,col].map(ids[col])
        chunk["id"] = np.arange(chunk.shape[0]) + i*CHUNK_SIZE + 1 + start_id
        chunk["day"] = chunk["hour"].map(lambda v: int(str(v)[-4:-2]))
        chunk["hour"] = chunk["hour"].map(lambda v: int(str(v)[-2:]))
        
        if "click" not in chunk.columns:
            chunk["click"] = 0
        chunk = chunk.ix[:,COLS]

        if i == 0 and mode == "w":
            chunk.to_csv(output_path,index=False)
        else:            
            chunk.to_csv(output_path,index=False,mode="a",header=False)

    return chunk["id"].max()

if __name__ == "__main__":
    counters = create_counters()
    update_counter("data_raw/train.csv",counters)
    update_counter("data_raw/test.csv",counters)
    ids = convert_counts_to_id(counters)
    max_id = write_translated("data_raw/train.csv","data_raw/merged.csv",ids)    
    _ = write_translated("data_raw/test.csv","data_raw/merged.csv",ids,mode="a",start_id = max_id)
