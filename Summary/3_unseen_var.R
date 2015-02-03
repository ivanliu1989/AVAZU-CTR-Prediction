setwd('/Users/ivan/Work_directory/VAZU/')
setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/VAZU')
rm(list=ls()); gc()
require(data.table)

train_app <- data.frame(fread('other/train_df_app_split_smooth.csv',colClasses='character',header=T,na.strings = "")) # 14596137
test_app <- data.frame(fread('other/test_df_app_split_smooth.csv',colClasses='character',header=T,na.strings = "")) # 1719304

# train_app <- data.frame(fread('other/train_df_site_split_smooth.csv',colClasses='character',header=T)) # 25832830
# test_app <- data.frame(fread('other/test_df_site_split_smooth.csv',colClasses='character',header=T)) # 2858160

for (n in 3:length(colnames(train_app))){
    
    val_list <- table(train_app[,n])
    val_list_t <- table(test_app[,n-1])
    val_list_final <- names(val_list_t)[which(!names(val_list_t) %in% names(val_list))]
    test_app[which(test_app[,n-1] %in% val_list_final),n-1] <- 'other'
        
    gc()
    print(paste('Feature',colnames(train_app)[n],'finished.', length(val_list_final), 'features removed!'))
    }
}

write.csv(test_app, file = 'data/test_df_app_split_smooth.csv', quote = F, row.names = F)
# write.csv(test_app, file = 'data/test_df_site_split_smooth.csv', quote = F, row.names = F)
