setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

options(scipen=888)
require(data.table)
pred_1 <- data.frame(fread('ensemble/submission_py_site_app_0.14_1_1_1_s5.csv'))
pred_2 <- data.frame(fread('ensemble/submit_xgboost_app_site_1.csv'))

identical(pred_1$id, pred_2$id)

pred_ensemble <- 0.5 * pred_1[,2] + 0.5 * pred_2[,2]
new_pred <- cbind.data.frame(id = pred_1[,1], click = pred_ensemble)

identical(new_pred$id, pred_2$id)
head(new_pred);head(pred_1);head(pred_2)

write.table(new_pred, file='submission_py_vw.csv',sep = ',', row.names = F)

pred_3 <- data.frame(fread('submission_py_vw.csv'))
head(pred_3,100)

class(pred_3[,2])


### merge by col ### 
total <- merge(pred_1,pred_2,by=c("id"))
head(total)
total$click <- 0.5*total[,2]+0.5*total[,3]
total <- total[,-c(2,3)]

write.table(total, file='ensemble/submission_ensemble.csv',sep = ',', row.names = F)
