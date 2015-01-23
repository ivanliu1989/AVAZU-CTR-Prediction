rm(list=ls())

## library(randomForest)
## library(ROCR)
## library(foreach)
## library(doParallel)
## library(nnet)
library(glmnet)



test <- read.csv("test.csv", header=TRUE)

train <- read.csv("train.csv", header=TRUE)

for (i in seq(dim(train)[2])){

train[[i]] <- as.factor(train[[i]])

}




for (i in seq(dim(test)[2])){

test[[i]] <- as.factor(test[[i]])

}





X = sparse.model.matrix(as.formula(paste("ACTION ~", paste(colnames(train[,-1]),
    sep = "", collapse=" +"))), data = train)

 model = cv.glmnet(X, train[,1], family = "binomial")

print("glmnet model completed")



predict(model,newx=test[,2:10], s="lambda.min")

print("So far so good")
