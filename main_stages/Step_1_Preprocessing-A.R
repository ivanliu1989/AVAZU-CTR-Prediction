# setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/FICO/Helping-Santas-Helpers')
# setwd('H:/Machine_Learning/VAZU')
setwd('/Users/ivan/Work_directory/VAZU')
gc(); rm(list=ls())
require(data.table)

### DOW, Hour, Holiday ###
train <- as.data.frame(fread('data/train',stringsAsFactors = F))
head(train,10);dim(train)
table(train$date)

train$date <- substr(train$hour,5,6)
train$hour <- substr(train$hour,7,8)

train[which(train$date %in% c(27)),25] <- 1 # Mon
train[which(train$date %in% c(21,28)),25] <- 2 # Tue
train[which(train$date %in% c(22,29)),25] <- 3 # Wed
train[which(train$date %in% c(23,30)),25] <- 4 # Thu
train[which(train$date %in% c(24)),25] <- 5 # Fri
train[which(train$date %in% c(25)),25] <- 6 # Sat
train[which(train$date %in% c(26)),25] <- 7 # Sun

summary(train)
