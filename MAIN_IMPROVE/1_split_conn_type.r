setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/VAZU')
setwd('H:/Machine_Learning/VAZU/')

gc(); rm(list=ls());
require(data.table); require(caret)


train <- data.frame(fread('data/train_df_site_smooth.csv'))
test <- data.frame(fread('data/test_df_site_smooth.csv'))

train <- data.frame(fread('data/train_df_app_smooth.csv'))
test <- data.frame(fread('data/test_df_app_smooth.csv'))


head(train)
head(test)
table(train$device_conn_type)
table(test$device_conn_type)
sum(is.na(train$device_conn_type))
sum(is.na(test$device_conn_type))
which(train$device_conn_type=='')
which(test$device_conn_type=='')

### site
#device_type
# 0        1        2        4        5 
# 1939431 23892993       31       40      335 
# 0       1       4       5 
# 146844 2711307       2       7 

#device_conn_type
# 0        2 
# 24812979  1019851 
# 0       2 
# 2712486  145674 


### app
#device_type
# 0        1        4        5 
# 281381 13411674   774232   128850 
# 0       1       4       5 
# 20581 1631472   57875    9376 

#device_conn_type
# 0        2        3        5 
# 10073859  2297592  2181796    42890 
# 0       2       3       5 
# 1145993  314173  249814    9324 