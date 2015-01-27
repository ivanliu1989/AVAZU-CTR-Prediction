setwd('H:/Machine_Learning/VAZU/')
setwd('/Users/ivan/Work_directory/VAZU/')
gc(); rm(list=ls());
require(data.table); 

train <- data.frame(fread('data/train_df_site_split.csv'))
test <- data.frame(fread('data/test_df_site_split.csv'))

train <- data.frame(fread('data/train_df_app_split.csv'))
test <- data.frame(fread('data/test_df_app_split.csv'))

head(train);head(test)

# img_size
img_size_train <- table(train$img_size)
length(train$img_size);length(img_size_train);sum(is.na(train$img_size))
length(table(train[-which(train$img_size %in% test$img_size),'img_size']))
img_size_test <- table(test$img_size)
length(test$img_size);length(img_size_test);sum(is.na(test$img_size)); 
length(table(test[-which(test$img_size %in% train$img_size),'img_size']))

# device_id_2
device_id_2_train <- table(train$device_id_2)
length(train$device_id_2);length(device_id_2_train);sum(is.na(train$device_id_2))
length(table(train[-which(train$device_id_2 %in% test$device_id_2),'device_id_2']))
device_id_2_test <- table(test$device_id_2)
length(test$device_id_2);length(device_id_2_test);sum(is.na(test$device_id_2)); 
length(table(test[-which(test$device_id_2 %in% train$device_id_2),'device_id_2']))
# device_id_3
device_id_3_train <- table(train$device_id_3)
length(train$device_id_3);length(device_id_3_train);sum(is.na(train$device_id_3))
length(table(train[-which(train$device_id_3 %in% test$device_id_3),'device_id_3']))
device_id_3_test <- table(test$device_id_3)
length(test$device_id_3);length(device_id_3_test);sum(is.na(test$device_id_3)); 
length(table(test[-which(test$device_id_3 %in% train$device_id_3),'device_id_3']))

# device_ip_2
device_ip_2_train <- table(train$device_ip_2)
length(train$device_ip_2);length(device_ip_2_train);sum(is.na(train$device_ip_2))
length(table(train[-which(train$device_ip_2 %in% test$device_ip_2),'device_ip_2']))
device_ip_2_test <- table(test$device_ip_2)
length(test$device_ip_2);length(device_ip_2_test);sum(is.na(test$device_ip_2)); 
length(table(test[-which(test$device_ip_2 %in% train$device_ip_2),'device_ip_2']))
# device_ip_3
device_ip_3_train <- table(train$device_ip_3)
length(train$device_ip_3);length(device_ip_3_train);sum(is.na(train$device_ip_3))
length(table(train[-which(train$device_ip_3 %in% test$device_ip_3),'device_ip_3']))
device_ip_3_test <- table(test$device_ip_3)
length(test$device_ip_3);length(device_ip_3_test);sum(is.na(test$device_ip_3)); 
length(table(test[-which(test$device_ip_3 %in% train$device_ip_3),'device_ip_3']))