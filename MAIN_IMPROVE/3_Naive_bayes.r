setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/VAZU')
gc(); rm(list=ls());
require(data.table);require(RMOA); require(caret)

train_app <- data.frame(fread('data/train_df_app_smooth.csv'))
train_app <- train_app[,-1]
head(train_app)

for (i in seq(dim(train_app)[2])){   
    train_app[which(train_app[[i]]==''),i] <- NaN   
}
for (i in seq(dim(train_app)[2])){   
    train_app[[i]] <- as.factor(train_app[[i]])   
}

# index <- createFolds(y = train_app$click, k = 10, list = F, returnTrain = FALSE)
index <- createDataPartition(y = train_app$click, p = 0.8, list = F)
train_dt <- train_app[index,]
test_dt <- train_app[-index,]
dim(train_dt);dim(test_dt);dim(train_app)
rm(train_app)

### Naive Bayes ###
## Define a stream - e.g. a stream based on a data.frame
# factorise(x=train_app)
train_dt <- datastream_dataframe(data=train_dt)
train_dt$get_points(10)


## Train the HoeffdingTree on the iris dataset
ctrl <- MOAoptions(model = "NaiveBayes")
mymodel <- NaiveBayes(control=ctrl)
mymodel

mytrainedmodel <- trainMOA(model = mymodel, chunksize = 10000, 
                           click ~ ., data = train_dt)
train_dt$reset()
mytrainedmodel$model

## Predict using the HoeffdingTree on the iris dataset
save(mytrainedmodel, file='naivebayes_model_app.RData')
scores <- predict(mytrainedmodel, newdata=test_dt, type="response")
str(scores)
LogLoss(scores, test_dt$click)
scores <- predict(mytrainedmodel, newdata=test_dt, type="votes")
head(scores)

## logloss func
LogLoss<-function(predicted,actual)
{
    result<- -1/length(actual)*(sum((actual*log(predicted)+(1-actual)*log(1-predicted))))
    return(result)
}