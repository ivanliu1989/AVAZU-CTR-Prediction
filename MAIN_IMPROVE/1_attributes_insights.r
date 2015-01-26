setwd('H:/Machine_Learning/VAZU/')

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

# id
id_train <- table(train$id)
length(train$id);length(id_train);sum(is.na(train$id))
id_test <- table(test$id)
length(test$id);length(id_test);sum(is.na(test$id))
# click
click_train <- table(train$click)
length(train$click);length(click_train);sum(is.na(train$click))
# hour
hour_train <- table(train$hour)
length(train$hour);length(hour_train);sum(is.na(train$hour))
hour_test <- table(test$hour)
length(test$hour);length(hour_test);sum(is.na(test$hour))
# C1
C1_train <- table(train$C1)
length(train$C1);length(C1_train);sum(is.na(train$C1))
C1_test <- table(test$C1)
length(test$C1);length(C1_test);sum(is.na(test$C1))
# banner_pos
banner_pos_train <- table(train$banner_pos)
length(train$banner_pos);length(banner_pos_train);sum(is.na(train$banner_pos))
banner_pos_test <- table(test$banner_pos)
length(test$banner_pos);length(banner_pos_test);sum(is.na(test$banner_pos))
# app_id
app_id_train <- table(train$app_id)
length(train$app_id);length(app_id_train);sum(is.na(train$app_id))
length(table(train[-which(train$app_id %in% test$app_id),'app_id']))
app_id_test <- table(test$app_id)
length(test$app_id);length(app_id_test);sum(is.na(test$app_id)); 
length(table(test[-which(test$app_id %in% train$app_id),'app_id']))
# app_domain
app_domain_train <- table(train$app_domain)
length(train$app_domain);length(app_domain_train);sum(is.na(train$app_domain))
length(table(train[-which(train$app_domain %in% test$app_domain),'app_domain']))
app_domain_test <- table(test$app_domain)
length(test$app_domain);length(app_domain_test);sum(is.na(test$app_domain)); 
length(table(test[-which(test$app_domain %in% train$app_domain),'app_domain']))
# app_category
app_category_train <- table(train$app_category)
length(train$app_category);length(app_category_train);sum(is.na(train$app_category))
length(table(train[-which(train$app_category %in% test$app_category),'app_category']))
app_category_test <- table(test$app_category)
length(test$app_category);length(app_category_test);sum(is.na(test$app_category)); 
length(table(test[-which(test$app_category %in% train$app_category),'app_category']))
# device_id
device_id_train <- table(train$device_id)
length(train$device_id);length(device_id_train);sum(is.na(train$device_id))
length(table(train[-which(train$device_id %in% test$device_id),'device_id']))
device_id_test <- table(test$device_id)
length(test$device_id);length(device_id_test);sum(is.na(test$device_id)); 
length(table(test[-which(test$device_id %in% train$device_id),'device_id']))
# device_ip
device_ip_train <- table(train$device_ip)
length(train$device_ip);length(device_ip_train);sum(is.na(train$device_ip))
length(table(train[-which(train$device_ip %in% test$device_ip),'device_ip']))
device_ip_test <- table(test$device_ip)
length(test$device_ip);length(device_ip_test);sum(is.na(test$device_ip)); 
length(table(test[-which(test$device_ip %in% train$device_ip),'device_ip']))
# device_model
device_model_train <- table(train$device_model)
length(train$device_model);length(device_model_train);sum(is.na(train$device_model))
length(table(train[-which(train$device_model %in% test$device_model),'device_model']))
device_model_test <- table(test$device_model)
length(test$device_model);length(device_model_test);sum(is.na(test$device_model)); 
length(table(test[-which(test$device_model %in% train$device_model),'device_model']))
# device_type
device_type_train <- table(train$device_type)
length(train$device_type);length(device_type_train);sum(is.na(train$device_type))
length(table(train[-which(train$device_type %in% test$device_type),'device_type']))
device_type_test <- table(test$device_type)
length(test$device_type);length(device_type_test);sum(is.na(test$device_type)); 
length(table(test[-which(test$device_type %in% train$device_type),'device_type']))
# device_conn_type
device_conn_type_train <- table(train$device_conn_type)
length(train$device_conn_type);length(device_conn_type_train);sum(is.na(train$device_conn_type))
length(table(train[-which(train$device_conn_type %in% test$device_conn_type),'device_conn_type']))
device_conn_type_test <- table(test$device_conn_type)
length(test$device_conn_type);length(device_conn_type_test);sum(is.na(test$device_conn_type)); 
length(table(test[-which(test$device_conn_type %in% train$device_conn_type),'device_conn_type']))
# C14
C14_train <- table(train$C14)
length(train$C14);length(C14_train);sum(is.na(train$C14))
length(table(train[-which(train$C14 %in% test$C14),'C14']))
C14_test <- table(test$C14)
length(test$C14);length(C14_test);sum(is.na(test$C14)); 
length(table(test[-which(test$C14 %in% train$C14),'C14']))
# C15
C15_train <- table(train$C15)
length(train$C15);length(C15_train);sum(is.na(train$C15))
length(table(train[-which(train$C15 %in% test$C15),'C15']))
C15_test <- table(test$C15)
length(test$C15);length(C15_test);sum(is.na(test$C15)); 
length(table(test[-which(test$C15 %in% train$C15),'C15']))
# C16
C16_train <- table(train$C16)
length(train$C16);length(C16_train);sum(is.na(train$C16))
length(table(train[-which(train$C16 %in% test$C16),'C16']))
C16_test <- table(test$C16)
length(test$C16);length(C16_test);sum(is.na(test$C16)); 
length(table(test[-which(test$C16 %in% train$C16),'C16']))
# C17
C17_train <- table(train$C17)
length(train$C17);length(C17_train);sum(is.na(train$C17))
length(table(train[-which(train$C17 %in% test$C17),'C17']))
C17_test <- table(test$C17)
length(test$C17);length(C17_test);sum(is.na(test$C17)); 
length(table(test[-which(test$C17 %in% train$C17),'C17']))
# C18
C18_train <- table(train$C18)
length(train$C18);length(C18_train);sum(is.na(train$C18))
length(table(train[-which(train$C18 %in% test$C18),'C18']))
C18_test <- table(test$C18)
length(test$C18);length(C18_test);sum(is.na(test$C18)); 
length(table(test[-which(test$C18 %in% train$C18),'C18']))
# C19
C19_train <- table(train$C19)
length(train$C19);length(C19_train);sum(is.na(train$C19))
length(table(train[-which(train$C19 %in% test$C19),'C19']))
C19_test <- table(test$C19)
length(test$C19);length(C19_test);sum(is.na(test$C19)); 
length(table(test[-which(test$C19 %in% train$C19),'C19']))
# C20
C20_train <- table(train$C20)
length(train$C20);length(C20_train);sum(is.na(train$C20))
length(table(train[-which(train$C20 %in% test$C20),'C20']))
C20_test <- table(test$C20)
length(test$C20);length(C20_test);sum(is.na(test$C20)); 
length(table(test[-which(test$C20 %in% train$C20),'C20']))
# C21
C21_train <- table(train$C21)
length(train$C21);length(C21_train);sum(is.na(train$C21))
length(table(train[-which(train$C21 %in% test$C21),'C21']))
C21_test <- table(test$C21)
length(test$C21);length(C21_test);sum(is.na(test$C21)); 
length(table(test[-which(test$C21 %in% train$C21),'C21']))