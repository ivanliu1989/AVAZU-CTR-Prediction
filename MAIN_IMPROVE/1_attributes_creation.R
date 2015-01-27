setwd('H:/Machine_Learning/VAZU/')
setwd('/Users/ivan/Work_directory/VAZU/')
rm(list=ls());gc(); 
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

device_id_train_trunc <- substr(train$device_id, 5, 8) ### perfect matching (site, 0)!!! 1-4; 5-8
device_id_test_trunc <- substr(test$device_id, 5, 8) ### perfect matching (app, 0)!!! 1-4; 5-8
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

device_ip_train_trunc <- substr(train$device_ip, 1, 4) ### perfect matching (site, 4250/471248)!!! 1-4; 5-8
device_ip_test_trunc <- substr(test$device_ip, 1, 4) ### good matching (app, 20457/395724; 0/65491)!!! 1-4; 5-8
device_ip_train_trunc_tb <- table(device_ip_train_trunc)
device_ip_test_trunc_tb <- table(device_ip_test_trunc)
length(device_ip_train_trunc);length(device_ip_train_trunc_tb);
length(table(device_ip_train_trunc[-which(device_ip_train_trunc %in% device_ip_test_trunc)]))
length(device_ip_test_trunc);length(device_ip_test_trunc_tb);
length(table(device_ip_test_trunc[-which(device_ip_test_trunc %in% device_ip_train_trunc)]))

# site_domain
site_domain_train <- table(train$site_domain)
length(train$site_domain);length(site_domain_train);sum(is.na(train$site_domain))
length(table(train[-which(train$site_domain %in% test$site_domain),'site_domain']))
site_domain_test <- table(test$site_domain)
length(test$site_domain);length(site_domain_test);sum(is.na(test$site_domain)); 
length(table(test[-which(test$site_domain %in% train$site_domain),'site_domain']))

site_domain_train_trunc <- substr(train$site_domain, 7, 8) ### perfect matching (site, 4250/471248)!!! 1-4; 5-8
site_domain_test_trunc <- substr(test$site_domain, 7, 8) ### good matching (app, 20457/395724; 0/65491)!!! 1-4; 5-8
site_domain_train_trunc_tb <- table(site_domain_train_trunc)
site_domain_test_trunc_tb <- table(site_domain_test_trunc)
length(site_domain_train_trunc);length(site_domain_train_trunc_tb);
length(table(site_domain_train_trunc[-which(site_domain_train_trunc %in% site_domain_test_trunc)]))
length(site_domain_test_trunc);length(site_domain_test_trunc_tb);
length(table(site_domain_test_trunc[-which(site_domain_test_trunc %in% site_domain_train_trunc)]))

# site_id
site_id_train <- table(train$site_id)
length(train$site_id);length(site_id_train);sum(is.na(train$site_id))
length(table(train[-which(train$site_id %in% test$site_id),'site_id']))
site_id_test <- table(test$site_id)
length(test$site_id);length(site_id_test);sum(is.na(test$site_id)); 
length(table(test[-which(test$site_id %in% train$site_id),'site_id']))

site_id_train_trunc <- substr(train$site_id, 3, 6) ### perfect matching (site, 4250/471248)!!! 1-4; 5-8
site_id_test_trunc <- substr(test$site_id, 3, 6) ### good matching (app, 20457/395724; 0/65491)!!! 1-4; 5-8
site_id_train_trunc_tb <- table(site_id_train_trunc)
site_id_test_trunc_tb <- table(site_id_test_trunc)
length(site_id_train_trunc);length(site_id_train_trunc_tb);
length(table(site_id_train_trunc[-which(site_id_train_trunc %in% site_id_test_trunc)]))
length(site_id_test_trunc);length(site_id_test_trunc_tb);
length(table(site_id_test_trunc[-which(site_id_test_trunc %in% site_id_train_trunc)]))

# app_domain
app_domain_train <- table(train$app_domain)
length(train$app_domain);length(app_domain_train);sum(is.na(train$app_domain))
length(table(train[-which(train$app_domain %in% test$app_domain),'app_domain']))
app_domain_test <- table(test$app_domain)
length(test$app_domain);length(app_domain_test);sum(is.na(test$app_domain)); 
length(table(test[-which(test$app_domain %in% train$app_domain),'app_domain']))

app_domain_train_trunc <- substr(train$app_domain, 1, 2) ### perfect matching (app, 4250/471248)!!! 1-4; 5-8
app_domain_test_trunc <- substr(test$app_domain, 1, 2) ### good matching (app, 20457/395724; 0/65491)!!! 1-4; 5-8
app_domain_train_trunc_tb <- table(app_domain_train_trunc)
app_domain_test_trunc_tb <- table(app_domain_test_trunc)
length(app_domain_train_trunc);length(app_domain_train_trunc_tb);
length(table(app_domain_train_trunc[-which(app_domain_train_trunc %in% app_domain_test_trunc)]))
length(app_domain_test_trunc);length(app_domain_test_trunc_tb);
length(table(app_domain_test_trunc[-which(app_domain_test_trunc %in% app_domain_train_trunc)]))

# app_id
app_id_train <- table(train$app_id)
length(train$app_id);length(app_id_train);sum(is.na(train$app_id))
length(table(train[-which(train$app_id %in% test$app_id),'app_id']))
app_id_test <- table(test$app_id)
length(test$app_id);length(app_id_test);sum(is.na(test$app_id)); 
length(table(test[-which(test$app_id %in% train$app_id),'app_id']))

app_id_train_trunc <- substr(train$app_id, 1, 2) ### perfect matching (app, 4250/471248)!!! 1-4; 5-8
app_id_test_trunc <- substr(test$app_id, 1, 2) ### good matching (app, 20457/395724; 0/65491)!!! 1-4; 5-8
app_id_train_trunc_tb <- table(app_id_train_trunc)
app_id_test_trunc_tb <- table(app_id_test_trunc)
length(app_id_train_trunc);length(app_id_train_trunc_tb);
length(table(app_id_train_trunc[-which(app_id_train_trunc %in% app_id_test_trunc)]))
length(app_id_test_trunc);length(app_id_test_trunc_tb);
length(table(app_id_test_trunc[-which(app_id_test_trunc %in% app_id_train_trunc)]))

