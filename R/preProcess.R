setwd('H:/Machine_Learning/VAZU')
gc(); rm(list=ls())
require(data.table); require(caret)

train <- as.data.frame(fread('data/train.csv',stringsAsFactors = F))
test <- as.data.frame(fread('data/test.csv',stringsAsFactors = F))
