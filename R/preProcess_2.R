setwd('H:/Machine_Learning/VAZU/')

gc(); rm(list=ls());
require(data.table); require(caret)


train <- data.frame(fread('data/ex/train_df_site_smooth.csv'))
test <- data.frame(fread('data/ex/test_df_site_smooth_ex.csv'))

train <- data.frame(fread('data/ex/train_df_app_smooth.csv'))
test <- data.frame(fread('data/ex/test_df_app_smooth_ex.csv'))

train <- train[,-c(1,2)]
test <- test[,-c(1)]
dt <- rbind(train, test)
head(dt)
rm(train);rm(test)

### Site ###
device_ip <- sort(which(table(dt[8])==1)) # device_ip
head(device_ip) # 0000cdad 00013a26 00021804 000248eb 00025abd 0002e212
tail(device_ip)

which(table(dt[19])==1) #C21: 184

### App ###

which(table(dt[19])==1) 

