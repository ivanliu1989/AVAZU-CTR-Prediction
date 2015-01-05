setwd('/Users/ivan/Work_directory/VAZU/')
setwd('H:/Machine_Learning/VAZU/')
gc(); rm(list=ls());

pred_1 <- read.csv('submission.csv')
pred_2 <- read.csv('submission_0391171.csv')

identical(pred_1$id, pred_2$id)

pred_ensemble <- pred_1
pred_ensemble$click <- 0.5 * pred_1$click + 0.5 * pred_2$click

head(pred_ensemble);head(pred_1);head(pred_2)

write.csv(pred_ensemble, file='submission_py_vw.csv',quote = F, row.names = F)

pred_3 <- read.csv('submission_py_vw.csv')
head(pred_3)
