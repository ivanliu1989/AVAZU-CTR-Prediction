# setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/FICO/Helping-Santas-Helpers')
setwd('H:/Machine_Learning/VAZU')
gc(); rm(list=ls())
require(data.table); require(caret)

train <- as.data.frame(fread('data/train.csv',stringsAsFactors = F))
train <- train[,-1]
summary(train)

index <- createDataPartition(y = train$click, p = 0.8, list = F)
train_dt <- train[index,]
test_dt <- train[-index,]
dim(train_dt);dim(test_dt);dim(train)
rm(train)

## basic ##
fitControl <- trainControl(method = "repeatedcv",number = 10,repeats = 5,
                           ## Estimate class probabilities
                           classProbs = TRUE,
                           ## Evaluate performance using 
                           ## the following function
                           summaryFunction = twoClassSummary)
gbmGrid <-  expand.grid(interaction.depth = c(1, 5, 9),
                        n.trees = (1:30)*50,
                        shrinkage = 0.1)
set.seed(825)
svmFit <- train(click~., data=train_dt, method = "gbm",
                trControl = fitControl, tuneGrid = gbmGrid, metric = "ROC")

testPred <- predict(svmFit, test_dt, type = "prob")
postResample(testPred, test_dt$click)
sensitivity(testPred, test_dt$click)
confusionMatrix(testPred, test_dt$click)
getTrainPerf(svmFit)


## adaptive ## 
fitControl2 <- trainControl(method = "adaptive_cv",number = 10,repeats = 5,
                            ## Estimate class probabilities
                            classProbs = TRUE,
                            ## Evaluate performance using 
                            ## the following function
                            summaryFunction = twoClassSummary,
                            ## Adaptive resampling information:
                            adaptive = list(min = 10,alpha = 0.05,method = "gls",complete = TRUE))

set.seed(825)
svmFit2 <- train(train_dt$click ~. , method = "svmRadial",trControl = fitControl2,
                 preProc = c("center", "scale"),tuneLength = 8,metric = "ROC")