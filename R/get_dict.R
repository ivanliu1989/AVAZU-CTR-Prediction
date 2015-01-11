# setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

options(scipen=888)
require(data.table); require(Matrix)
train <- as.data.frame(fread('data/onehot/train_df_smooth_hash_app.csv')) # train_df_site_smooth
test <- as.data.frame(fread('data/onehot/test_df_smooth_hash_app.csv')) # test_df_site_smooth

### preparison ###
train_id_click <- train[c('id','click')]; head(train_id)
test_id <- test['id']; head(test_id)
train <- train[,-c(1,2)]; head(train)
test <- test[,-1]; head(test)
train <- rbind(train,test); head(train); tail(train)
rm(test)

for (i in seq(dim(train)[2])){   
    train[which(train[[i]]==''),i] <- NaN   
}
for (i in seq(dim(train)[2])){   
    train[[i]] <- as.factor(train[[i]])   
}

var_dict <- c()
for (i in seq(dim(train)[2])){   
    var_dict <- c(var_dict, levels(train[,i]))   
} 

length(var_dict)
length(table(var_dict))

var_dict_df <- data.frame(key=0:(length(var_dict)-1), val=var_dict)
head(var_dict_df)

write.csv(var_dict_df, file = 'data/onehot/train_df_app_dict.csv', quote = F, row.names = F)
