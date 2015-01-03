# setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/FICO/Helping-Santas-Helpers')
setwd('H:/Machine_Learning/VAZU')
gc(); rm(list=ls())
require(data.table)

train <- fread('data/train.csv',stringsAsFactors = F)