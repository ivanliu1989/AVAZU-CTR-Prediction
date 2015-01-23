rm(list = ls(all = TRUE))

library(gbm)

##set the seed

set.seed(123)

test=read.csv("test.csv",stringsAsFactors=F)

spltest=sapply(test,is.numeric)
test1=test[,spltest]

test1[test1=="-1"]=0
test1$C20=as.integer(test1$C20)

xTest=as.matrix(test1)

train=read.csv("train.csv",nrow=1000000,stringsAsFactors=F)
y=train$click

spltrain=sapply(train,is.numeric)
train1=train[,spltrain]

train1[train1=="-1"]=0
train1$C20=as.integer(train1$C20)

train1$click=NULL
xTrain=as.matrix(train1)
	
gbm1 <- gbm.fit(x=xTrain, y=y,distribution = "poisson",n.trees = 10,interaction.depth = 40,n.minobsinnode = 				100,shrinkage =.1,bag.fraction = .5)
pred <- predict(gbm1,xTest,type="response",n.trees=10)

w <- p <- list()

for(i in (1:10))
{
    	train01=read.csv("train.csv",nrow=1000000,stringsAsFactors=F, skip= (i-1) * 1000000,header=F)
	names(train01)=names(train)	
	y=train01$click
	

	spltrain=sapply(train01,is.numeric)
	train1=train01[,spltrain]

	train1[train1=="-1"]=0
	train1$C20=as.integer(train1$C20)

	train1$click=NULL
	xTrain=as.matrix(train1)
	
	w[[i]] <- gbm.fit(x=xTrain, y=y,distribution = "poisson",n.trees = 10,interaction.depth = 40,n.minobsinnode = 				100,shrinkage =.1,bag.fraction = .5)
    	p[[i]] <- predict(w[[i]],xTest,type="response",n.trees=10)

	pred=(pred+p[[i]])/2

	
}
submission=data.frame(id=test$id,click=pred)
write.csv(submission,gzfile("mysubmission.csv.gz"),row.names=FALSE,quote=FALSE)


