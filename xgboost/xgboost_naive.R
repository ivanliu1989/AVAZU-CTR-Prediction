install.packages('xgboost')

setwd('H:/Machine_Learning/VAZU')
gc(); rm(list=ls())
require(data.table); require(caret);
require(methods); require(xgboost)

train <- as.data.frame(fread('data/train.csv',stringsAsFactors = F))
test <- as.data.frame(fread('data/test.csv',stringsAsFactors = F))

dtrain <- xgb.DMatrix(data = train[,-c(1:2)], label = train$click)
bst <- xgboost(data = dtrain, max.depth = 2, eta = 1, nround = 2, objective = "binary:logistic")

#-------------Basic Training using XGBoost-----------------
print ('train xgboost with verbose 0, no message')
bst <- xgboost(data = dtrain, max.depth = 2, eta = 1, nround = 2,
               objective = "binary:logistic", verbose = 0)
print ('train xgboost with verbose 1, print evaluation metric')
bst <- xgboost(data = dtrain, max.depth = 2, eta = 1, nround = 2,
               objective = "binary:logistic", verbose = 1)
print ('train xgboost with verbose 2, also print information about tree')
bst <- xgboost(data = dtrain, max.depth = 2, eta = 1, nround = 2,
               objective = "binary:logistic", verbose = 2)

# LibSVM format
# bst <- xgboost(data = 'agaricus.train.svm', max.depth = 2, eta = 1, nround = 2,objective = "binary:logistic")

#--------------------basic prediction using xgboost--------------
# you can do prediction using the following line
# you can put in Matrix, sparseMatrix, or xgb.DMatrix 
pred <- predict(bst, test$data)
err <- mean(as.numeric(pred > 0.5) != test$label)
print(paste("test-error=", err))

#-------------------save and load models-------------------------
# save model to binary local file
xgb.save(bst, "xgboost.model")
# load binary model to R
bst2 <- xgb.load("xgboost.model")
pred2 <- predict(bst2, test$data)
# pred2 should be identical to pred
print(paste("sum(abs(pred2-pred))=", sum(abs(pred2-pred))))

#----------------Advanced features --------------
# to use advanced features, we need to put data in xgb.DMatrix
dtrain <- xgb.DMatrix(data = train$data, label=train$label)
dtest <- xgb.DMatrix(data = test$data, label=test$label)
#---------------Using watchlist----------------
# watchlist is a list of xgb.DMatrix, each of them tagged with name
watchlist <- list(train=dtrain, test=dtest)
# to train with watchlist, use xgb.train, which contains more advanced features
# watchlist allows us to monitor the evaluation result on all data in the list 
print ('train xgboost using xgb.train with watchlist')
bst <- xgb.train(data=dtrain, max.depth=2, eta=1, nround=2, watchlist=watchlist,
                 objective = "binary:logistic")
# we can change evaluation metrics, or use multiple evaluation metrics
print ('train xgboost using xgb.train with watchlist, watch logloss and error')
bst <- xgb.train(data=dtrain, max.depth=2, eta=1, nround=2, watchlist=watchlist,
                 eval.metric = "error", eval.metric = "logloss",
                 objective = "binary:logistic")

# xgb.DMatrix can also be saved using xgb.DMatrix.save
xgb.DMatrix.save(dtrain, "dtrain.buffer")
# to load it in, simply call xgb.DMatrix
dtrain2 <- xgb.DMatrix("dtrain.buffer")
bst <- xgb.train(data=dtrain2, max.depth=2, eta=1, nround=2, watchlist=watchlist,
                 objective = "binary:logistic")
# information can be extracted from xgb.DMatrix using getinfo
label = getinfo(dtest, "label")
pred <- predict(bst, dtest)
err <- as.numeric(sum(as.integer(pred > 0.5) != label))/length(label)
print(paste("test-error=", err))

# You can dump the tree you learned using xgb.dump into a text file
xgb.dump(bst, "dump.raw.txt", with.stats = T)

# Finally, you can check which features are the most important.
print("Most important features (look at column Gain):")
print(xgb.importance(feature_names = train$data@Dimnames[[2]], filename_dump = "dump.raw.txt"))