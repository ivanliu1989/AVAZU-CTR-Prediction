setwd('H:/Machine_Learning/VAZU/')

gc(); rm(list=ls());
require(data.table); 

train <- data.frame(fread('data/ex/train_df_site_smooth.csv'))
test <- data.frame(fread('data/ex/test_df_site_smooth_ex.csv'))

train <- data.frame(fread('data/ex/train_df_app_smooth.csv'))
test <- data.frame(fread('data/ex/test_df_app_smooth_ex.csv'))
