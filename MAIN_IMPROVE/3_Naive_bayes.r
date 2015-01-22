setwd('/Users/ivan/Work_directory/VAZU/')
gc(); rm(list=ls());
library(devtools)
install.packages("ff")
install.packages("rJava")
install_github("jwijffels/RMOA", subdir="RMOAjars/pkg")
install_github("jwijffels/RMOA", subdir="RMOA/pkg")

require(RMOA)

## Create a HoeffdingTree
hdt <- HoeffdingTree(numericEstimator = "GaussianNumericAttributeClassObserver")
hdt

## Define a stream - e.g. a stream based on a data.frame
data(iris)
iris <- factorise(iris)
irisdatastream <- datastream_dataframe(data=iris)

## Train the HoeffdingTree on the iris dataset
mymodel <- trainMOA(model = hdt, 
                    formula = Species ~ Sepal.Length + Sepal.Width + Petal.Length, 
                    data = irisdatastream)

## Predict using the HoeffdingTree on the iris dataset
scores <- predict(mymodel, newdata=iris, type="response")
str(scores)
table(scores, iris$Species)
scores <- predict(mymodel, newdata=iris, type="votes")
head(scores)


##
## Boosting example
##
irisdatastream$reset()
mymodel <- OzaBoost(baseLearner = "trees.HoeffdingTree", ensembleSize = 30)
mymodel <- trainMOA(model = mymodel, 
                    formula = Species ~ Sepal.Length + Sepal.Width + Petal.Length, 
                    data = irisdatastream)

## Predict using the HoeffdingTree on the iris dataset
scores <- predict(mymodel, newdata=iris, type="response")
str(scores)
table(scores, iris$Species)
scores <- predict(mymodel, newdata=iris, type="votes")
head(scores)