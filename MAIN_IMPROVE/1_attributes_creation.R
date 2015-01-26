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
