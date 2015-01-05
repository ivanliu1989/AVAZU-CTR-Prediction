setwd('H:/Machine_Learning/VAZU')
gc(); rm(list=ls())
require(data.table); require(caret)

train <- as.data.frame(fread('data/train.csv',stringsAsFactors = F))
test <- as.data.frame(fread('data/test.csv',stringsAsFactors = F))

head(train); head(test)

train_id <- train[,1]
train_label <- train[,2]
test_id <- test[,1]

train_data <- train[,-c(1,2)]
test_data <- test[,-1]

rm(train);rm(test)
head(train_data);head(test_data)

comb_dt <- rbind(train_data,test_data)
rm(train_data);rm(test_data);gc()

dim(comb_dt)
### hash tricks ###
install.packages('FeatureHashing')

### feature engineering ###
head(comb_dt)
comb_dt$date <- substr(comb_dt$hour,1,6)
