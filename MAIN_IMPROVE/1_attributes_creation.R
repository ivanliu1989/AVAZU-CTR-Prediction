setwd('H:/Machine_Learning/VAZU/')
setwd('/Users/ivan/Work_directory/VAZU/')
gc(); rm(list=ls());
require(data.table); 

train <- data.frame(fread('other/train_df_site.csv'))
test <- data.frame(fread('other/test_df_site.csv'))

train <- data.frame(fread('other/train_df_app.csv'))
test <- data.frame(fread('other/test_df_app.csv'))

for (i in seq(dim(train)[2])){   
    train[which(train[[i]]==''),i] <- NaN   
}
for (i in seq(dim(test)[2])){   
    test[which(test[[i]]==''),i] <- NaN   
}
head(train);head(test)

# device_id
device_id_train <- table(train$device_id)
length(train$device_id);length(device_id_train)
length(table(train[-which(train$device_id %in% test$device_id),'device_id']))
device_id_test <- table(test$device_id)
length(test$device_id);length(device_id_test)
length(table(test[-which(test$device_id %in% train$device_id),'device_id']))

device_id_train_trunc <- substr(train$device_id, 1, 4) ### perfect matching (site)!!!
device_id_test_trunc <- substr(test$device_id, 1, 4)
device_id_train_trunc_tb <- table(device_id_train_trunc)
device_id_test_trunc_tb <- table(device_id_test_trunc)
length(device_id_train_trunc);length(device_id_train_trunc_tb);
length(table(device_id_train_trunc[-which(device_id_train_trunc %in% device_id_test_trunc)]))
length(device_id_test_trunc);length(device_id_test_trunc_tb);
length(table(device_id_test_trunc[-which(device_id_test_trunc %in% device_id_train_trunc)]))

# device_ip
device_ip_train <- table(train$device_ip)
length(train$device_ip);length(device_ip_train);sum(is.na(train$device_ip))
length(table(train[-which(train$device_ip %in% test$device_ip),'device_ip']))
device_ip_test <- table(test$device_ip)
length(test$device_ip);length(device_ip_test);sum(is.na(test$device_ip)); 
length(table(test[-which(test$device_ip %in% train$device_ip),'device_ip']))

device_ip_train_trunc <- substr(train$device_ip, 1, 4) ### perfect matching (site)!!!
device_ip_test_trunc <- substr(test$device_ip, 1, 4)
device_ip_train_trunc_tb <- table(device_ip_train_trunc)
device_ip_test_trunc_tb <- table(device_ip_test_trunc)
length(device_ip_train_trunc);length(device_ip_train_trunc_tb);
length(table(device_ip_train_trunc[-which(device_ip_train_trunc %in% device_ip_test_trunc)]))
length(device_ip_test_trunc);length(device_ip_test_trunc_tb);
length(table(device_ip_test_trunc[-which(device_ip_test_trunc %in% device_ip_train_trunc)]))
