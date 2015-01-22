setwd('/Users/ivan/Work_directory/VAZU/')
gc(); rm(list=ls());
require(data.table);require(caret)

train_app <- data.frame(fread('data/train_df_app_smooth.csv'))
train_app <- train_app[,-1]
head(train_app)

for (i in seq(dim(train_app)[2])){   
    train_app[which(train_app[[i]]==''),i] <- NaN   
}
for (i in seq(dim(train_app)[2])){   
    train_app[[i]] <- as.factor(train_app[[i]])   
}

index <- createFolds(y = train_app$click, k = 10, list = F, returnTrain = FALSE)
#index <- createDataPartition(y = train_app$click, p = 0.8, list = F)
train_dt <- train_app[which(index==1),]
test_dt <- train_app[which(index==10),]
dim(train_dt);dim(test_dt);dim(train_app)
#rm(train_app)

### Naive Bayes ###
set.seed(825)

train_dt <- train_app[which(index==1),]

fit_app <- train(click~., data=train_dt, method = "nb")#,
                #trControl = fitControl, tuneGrid = gbmGrid, metric = "ROC")

testPred_app <- predict(fit_app, test_dt, type = "prob")