# setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

#options(scipen=888)
require(data.table); require(caret): require(Matrix)
train <- as.data.frame(fread('data/train_df_app_smooth.csv')) # train_df_site_smooth
test <- as.data.frame(fread('data/test_df_app_smooth.csv')) # test_df_site_smooth


### preparison ###
train_id <- train['id']; head(train_id)
test_id <- test['id']; head(test_id)
train <- train[,-1]; head(train)
test <- test[,-1]; head(test)
test['click'] <- 0
train <- rbind(train,test); head(train); tail(train)
rm(test)


### One-hot ###
options("contrasts") # the default:  "contr.treatment"
formula <- as.formula(paste("click ~ ", paste(colnames(train[,-1]), sep = "", collapse=" +")))
train_sparse <- sparse.model.matrix(formula, train)

for (i in seq(dim(train)[2])){   
    train[which(train[[i]]==''),i] <- NaN   
}
for (i in seq(dim(train)[2])){   
    train[[i]] <- as.factor(train[[i]])   
}

### app ###
one_hot_click <- train[colnames(train)[1]]
one_hot_1 <- sparse.model.matrix(~ -1 + colnames(train)[2], train[2], verbose=T)
one_hot_2 <- sparse.model.matrix(~ -1 + colnames(train)[3], train[3], verbose=T)
one_hot_3 <- sparse.model.matrix(~ -1 + colnames(train)[4], train[4], verbose=T)
one_hot_4 <- sparse.model.matrix(~ -1 + colnames(train)[5], train[5], verbose=T)
one_hot_5 <- sparse.model.matrix(~ -1 + colnames(train)[6], train[6], verbose=T)
one_hot_6 <- sparse.model.matrix(~ -1 + colnames(train)[7], train[7], verbose=T)
one_hot_7 <- sparse.model.matrix(~ -1 + colnames(train)[8], train[8], verbose=T)
one_hot_8 <- sparse.model.matrix(~ -1 + colnames(train)[9], train[9], verbose=T)
one_hot_9 <- sparse.model.matrix(~ -1 + colnames(train)[10], train[10], verbose=T)
one_hot_10 <- sparse.model.matrix(~ -1 + colnames(train)[11], train[11], verbose=T)
one_hot_11 <- sparse.model.matrix(~ -1 + colnames(train)[12], train[12], verbose=T)
one_hot_12 <- sparse.model.matrix(~ -1 + colnames(train)[13], train[13], verbose=T)
one_hot_13 <- sparse.model.matrix(~ -1 + colnames(train)[14], train[14], verbose=T)
one_hot_14 <- sparse.model.matrix(~ -1 + colnames(train)[15], train[15], verbose=T)
one_hot_15 <- sparse.model.matrix(~ -1 + colnames(train)[16], train[16], verbose=T)
one_hot_16 <- sparse.model.matrix(~ -1 + colnames(train)[17], train[17], verbose=T)
one_hot_17 <- sparse.model.matrix(~ -1 + colnames(train)[18], train[18], verbose=T)
one_hot_18 <- sparse.model.matrix(~ -1 + colnames(train)[19], train[19], verbose=T)
one_hot_19 <- sparse.model.matrix(~ -1 + colnames(train)[20], train[20], verbose=T)




### site ###