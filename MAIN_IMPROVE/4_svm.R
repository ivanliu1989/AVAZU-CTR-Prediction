setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

require(data.table); require(caret)
train <- data.frame(fread('data/train_df_app_smooth.csv'))
test <- data.frame(fread('data/test_df_app_smooth.csv'))

ID <- as.data.frame(train[,1])
train <- train[,-1]

index <- createDataPartition(train$click, p=0.8, list = F)
validation <- train[-index,]
train <- train[index,]
dim(validation);dim(train)
head(validation);head(train)

fitControl <- trainControl(method = "repeatedcv",
                           number = 10,
                           repeats = 5,
                           ## Estimate class probabilities
                           classProbs = TRUE,
                           ## Evaluate performance using 
                           ## the following function
                           summaryFunction = twoClassSummary)

set.seed(825)
svmFit <- train(click~., data=train,
                method = "svmRadial",
                trControl = fitControl,
                preProc = c("center", "scale"),
                tuneLength = 8,
                metric = "ROC")

gbmFit <- train(click ~ ., data = train,
                 method = "gbm",
                 trControl = fitControl,
                 ## This last option is actually one
                 ## for gbm() that passes through
                 verbose = T)

gc()
