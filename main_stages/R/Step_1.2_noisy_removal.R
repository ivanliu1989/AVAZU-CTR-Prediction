setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

options(scipen=888)
require(data.table)
train <- as.data.frame(fread('Data/train_df.csv'))
test <- as.data.frame(fread('Data/test_df.csv'))

train_id_click <- train[,c(1,2)]; head(train_id_click)
test_id <- test['id']; head(test_id)

train <- train[,-c(1,2)]; head(train)
test <- test[,-1]; head(test)

train <- rbind(train,test); head(train)
rm(test)

gc()

save(train_id_click, test_id, train, file='data/comb_data.RData')

### cleaning ###
df_col <- names(train)

del_item_4 <- names(which(table(train[,4])<=5))
train[which(train[,4] %in% del_item_4),4] <- del_item_4[1]

del_item_5 <- names(which(table(train[,5])<=5))
train[which(train[,5] %in% del_item_5),5] <- del_item_5[1]

del_item_6 <- names(which(table(train[,6])<=5))
train[which(train[,6] %in% del_item_6),6] <- del_item_6[1]

del_item_7 <- names(which(table(train[,7])<=5))
train[which(train[,7] %in% del_item_7),7] <- del_item_7[1]

del_item_8 <- names(which(table(train[,8])<=5))
train[which(train[,8] %in% del_item_8),8] <- del_item_8[1]

del_item_9 <- names(which(table(train[,9])<=5))
train[which(train[,9] %in% del_item_9),9] <- del_item_9[1]

del_item_10 <- names(which(table(train[,10])<=5))
train[which(train[,10] %in% del_item_10),10] <- del_item_10[1]

del_item_11 <- names(which(table(train[,11])<=5))
train[which(train[,11] %in% del_item_11),11] <- del_item_11[1]

del_item_12 <- names(which(table(train[,12])<=5))
train[which(train[,12] %in% del_item_12),12] <- del_item_12[1]

del_item_13 <- names(which(table(train[,13])<=5))
train[which(train[,13] %in% del_item_13),13] <- del_item_13[1]

del_item_14 <- names(which(table(train[,14])<=5))
train[which(train[,14] %in% del_item_14),14] <- del_item_14[1]

del_item_15 <- names(which(table(train[,15])<=5))
train[which(train[,15] %in% del_item_15),15] <- del_item_15[1]

del_item_16 <- names(which(table(train[,16])<=5))
train[which(train[,16] %in% del_item_16),16] <- del_item_16[1]

del_item_17 <- names(which(table(train[,17])<=5))
train[which(train[,17] %in% del_item_17),17] <- del_item_17[1]

del_item_18 <- names(which(table(train[,18])<=5))
train[which(train[,18] %in% del_item_18),18] <- del_item_18[1]

del_item_19 <- names(which(table(train[,19])<=5))
train[which(train[,19] %in% del_item_19),19] <- del_item_19[1]

del_item_20 <- names(which(table(train[,20])<=5))
train[which(train[,20] %in% del_item_20),20] <- del_item_20[1]

del_item_21 <- names(which(table(train[,21])<=5))
train[which(train[,21] %in% del_item_21),21] <- del_item_21[1]

del_item_22 <- names(which(table(train[,22])<=5))
train[which(train[,22] %in% del_item_22),22] <- del_item_22[1]


### split ###
dim(train_id_click)
dim(test_id)
dim(train)

test <- cbind(test_id,train[40428968:45006431,]); head(test); dim(test)
write.csv(as.data.frame(test), file = 'data/test_df_n.csv', quote = F, row.names = F)
rm(test)


save(train_id_click, train, file='data/train_data.RData')

gc(); rm(list=ls());
load('data/train_data.RData');gc()
train <- train[-c(40428968:45006431),]
train <- cbind(train_id_click, train); head(train); dim(train); gc()

save(train, file='data/train_df.RData')
load('data/train_df.RData');gc()
write.csv(as.data.frame(train), file = 'data/train_df_n.csv', quote = F, row.names = F)
rm(train)

train <- as.data.frame(fread('Data/train_df_n.csv'))
