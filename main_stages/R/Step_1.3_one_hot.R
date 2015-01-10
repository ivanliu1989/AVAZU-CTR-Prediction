# setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

#options(scipen=888)
require(data.table); require(caret): require(Matrix)
train <- as.data.frame(fread('data/train_df_app_smooth.csv')) # train_df_site_smooth
test <- as.data.frame(fread('data/test_df_app_smooth.csv')) # test_df_site_smooth

### preparison ###
train_id_click <- train[,c(1,2)]; head(train_id_click)
test_id <- test['id']; head(test_id)
train <- train[,-c(1,2)]; head(train)
test <- test[,-1];test <- test[,'index']; head(test)
train <- rbind(train,test); head(train)
rm(test)

### non-zero ###
nzv <- nearZeroVar(train, saveMetrics= TRUE)
nzv[nzv$nzv,][1:10,]
# nzv <- nearZeroVar(train)
# filteredDescr <- train[, -nzv]
# dim(filteredDescr)

### correlated var ###
descrCor2 <- cor(train)
summary(descrCor2[upper.tri(descrCor2)])
# highlyCorDescr <- findCorrelation(train, cutoff = .75)
# filteredDescr <- train[,-highlyCorDescr]

### One-hot ###
factor()
sparse.model.matrix()

dd <- data.frame(a = gl(3,4), b = gl(4,1,12))# balanced 2-way
options("contrasts") # the default:  "contr.treatment"
sparse.model.matrix(~ -1+ a + b, dd)# no intercept --> even sparser
