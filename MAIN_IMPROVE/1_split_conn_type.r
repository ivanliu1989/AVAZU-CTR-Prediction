setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/VAZU')
setwd('H:/Machine_Learning/VAZU/')

gc(); rm(list=ls());
require(data.table); require(caret)


train <- data.frame(fread('data/train_df_site_smooth.csv'))
test <- data.frame(fread('data/test_df_site_smooth.csv'))

train <- data.frame(fread('data/train_df_app_smooth.csv'))
test <- data.frame(fread('data/test_df_app_smooth.csv'))


head(train)
head(test)
table(train$device_ip)
table(test$device_ip)

