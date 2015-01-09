setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

options(scipen=888)
require(data.table); require(caret)
train <- as.data.frame(fread('data/train_df_app_smooth.csv')) # train_df_site_smooth
test <- as.data.frame(fread('data/test_df_app_smooth.csv')) # test_df_site_smooth

## preparison ##
train_id_click <- train[,c(1,2)]; head(train_id_click)
test_id <- test['id']; head(test_id)
train <- train[,-c(1,2)]; head(train)
test <- test[,-1]; head(test)
train <- rbind(train,test); head(train)
rm(test)


