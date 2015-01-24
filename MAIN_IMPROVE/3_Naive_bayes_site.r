Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre7') # for 64-bit version
setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/VAZU')
setwd('H:/Machine_Learning/VAZU/')

gc(); rm(list=ls());
require(data.table);require(RMOA); require(caret)

train_site <- data.frame(fread('data/train_df_site_smooth.csv'))
train_site <- train_site[,-1]
head(train_site)

for (i in seq(dim(train_site)[2])){   
    train_site[which(train_site[[i]]==''),i] <- NaN   
}
for (i in seq(dim(train_site)[2])){   
    train_site[[i]] <- as.factor(train_site[[i]])   
}

# index <- createFolds(y = train_site$click, k = 10, list = F, returnTrain = FALSE)
# index <- createDataPartition(y = train_site$click, p = 0.8, list = F)
# train_dt <- train_site[index,]
# test_dt <- train_site[-index,]
# dim(train_dt);dim(test_dt);dim(train_site)
# rm(train_site)

### Naive Bayes ###
## Define a stream - e.g. a stream based on a data.frame
# factorise(x=train_site)
train_site <- datastream_dataframe(data=train_site)
train_site$get_points(10)


## Train the HoeffdingTree on the iris dataset
ctrl <- MOAoptions(model = "NaiveBayes")
mymodel <- NaiveBayes(control=ctrl)

gc()
mytrainedmodel <- trainMOA(model = mymodel, chunksize = 1000000, 
                           click ~ ., data = train_site)
#train_site$reset()
mytrainedmodel$model
gc()
## Predict using the HoeffdingTree on the iris dataset
save(mytrainedmodel, file='naivebayes_model_site.RData')

test_site <- data.frame(fread('data/test_df_site_smooth.csv'))
test_site <- test_site[,-1]

for (i in seq(dim(test_site)[2])){   
    test_site[which(test_site[[i]]==''),i] <- NaN   
}
for (i in seq(dim(test_site)[2])){   
    test_site[[i]] <- as.factor(test_site[[i]])   
}

scores <- predict(mytrainedmodel, newdata=test_site, type="votes")

pred <- scores[,2]/(scores[,1]+scores[,2])
range(pred)
save(scores, file='naivebayes_pred_site.RData')
write.csv(pred,file='naive_bayes_site_pred.csv')

LogLoss(as.numeric(scores[,2])/(as.numeric(scores[,1])+as.numeric(scores[,2])), as.numeric(test_dt[1:100,1]))

## logloss func
LogLoss <- function(predicted,actual, eps=0.00001) {
    predicted <- pmin(pmax(predicted, eps), 1-eps)
    -1/length(actual)*(sum(actual*log(predicted)+(1-actual)*log(1-predicted)))
}