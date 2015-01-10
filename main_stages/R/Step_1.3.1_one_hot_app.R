# setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

#options(scipen=888)
require(data.table); require(caret): require(Matrix)
train <- as.data.frame(fread('data/train_df_app_smooth.csv')) # train_df_site_smooth
test <- as.data.frame(fread('data/test_df_app_smooth.csv')) # test_df_site_smooth


### preparison ###
train_id_click <- train[c('id','click')]; head(train_id)
test_id <- test['id']; head(test_id)
train <- train[,-c(1,2)]; head(train)
test <- test[,-1]; head(test)
train <- rbind(train,test); head(train); tail(train)
rm(test)


### One-hot ###
options("contrasts") # the default:  "contr.treatment"
formula <- as.formula(paste("~ ", paste(colnames(train), sep = "", collapse=" +")))
train_sparse <- sparse.model.matrix(formula, train)

for (i in seq(dim(train)[2])){   
    train[which(train[[i]]==''),i] <- NaN   
}
for (i in seq(dim(train)[2])){   
    train[[i]] <- as.factor(train[[i]])   
}
save(train_id_click, test_id, train, file='data/one_hot_prepare_app.RData')
#gc(); rm(list=ls());
#load('data/one_hot_prepare_app.RData')

### app ###
one_hot_1 <- model.matrix(~ -1 + hour, train[1], verbose=T);gc();train <- train[-1]
one_hot_2 <- model.matrix(~ -1 + C1, train[1], verbose=T);gc();train <- train[-1]
one_hot_3 <- model.matrix(~ -1 + banner_pos, train[1], verbose=T);gc();train <- train[-1]
one_hot_4 <- model.matrix(~ -1 + app_id, train[1], verbose=T);gc();train <- train[-1]
one_hot_5 <- model.matrix(~ -1 + app_domain, train[1], verbose=T);gc();train <- train[-1]
one_hot_6 <- model.matrix(~ -1 + app_category, train[1], verbose=T);gc();train <- train[-1]
one_hot_7 <- model.matrix(~ -1 + device_id, train[1], verbose=T);gc();train <- train[-1]
one_hot_8 <- model.matrix(~ -1 + device_ip, train[1], verbose=T);gc();train <- train[-1]
one_hot_9 <- model.matrix(~ -1 + device_model, train[1], verbose=T);gc();train <- train[-1]
one_hot_10 <- model.matrix(~ -1 + device_type, train[1], verbose=T);gc();train <- train[-1]
one_hot_11 <- model.matrix(~ -1 + device_conn_type, train[1], verbose=T);gc();train <- train[-1]
one_hot_12 <- model.matrix(~ -1 + C14, train[1], verbose=T);gc();train <- train[-1]
one_hot_13 <- model.matrix(~ -1 + C15, train[1], verbose=T);gc();train <- train[-1]
one_hot_14 <- model.matrix(~ -1 + C16, train[1], verbose=T);gc();train <- train[-1]
one_hot_15 <- model.matrix(~ -1 + C17, train[1], verbose=T);gc();train <- train[-1]
one_hot_16 <- model.matrix(~ -1 + C18, train[1], verbose=T);gc();train <- train[-1]
one_hot_17 <- model.matrix(~ -1 + C19, train[1], verbose=T);gc();train <- train[-1]
one_hot_18 <- model.matrix(~ -1 + C20, train[1], verbose=T);gc();train <- train[-1]
one_hot_19 <- model.matrix(~ -1 + C21, train[1], verbose=T);gc();train <- train[-1]

### save ###
one_hot_train <- cbind(one_hot_click, one_hot_1)
write.csv(one_hot_train, file = 'data/onehot_train_app.csv', quote = F, row.names = F)
#rm(one_hot_train)
