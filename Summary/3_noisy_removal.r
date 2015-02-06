setwd('/Users/ivan/Work_directory/VAZU/')
# setwd('C:/Users/Ivan.Liuyanfeng/Desktop/Data_Mining_Work_Space/VAZU')
rm(list=ls()); gc()
require(data.table)

# train_app <- data.frame(fread('other/train_df_app_split.csv',colClasses='character',header=T,na.strings = "")) # 14596137
# test_app <- data.frame(fread('other/test_df_app_split.csv',colClasses='character',header=T,na.strings = "")) # 1719304

train_app <- data.frame(fread('other/train_df_site_split.csv',colClasses='character',header=T,na.strings = "")) # 25832830
test_app <- data.frame(fread('other/test_df_site_split.csv',colClasses='character',header=T,na.strings = "")) # 2858160

ls();gc()
test_app$click <- 0

dim(train_app);dim(test_app)
train_app <- rbind(train_app,test_app)
#head(train_app)
rm(test_app);gc()

### remove ###
for (n in 3:length(colnames(train_app))){
    
    val_list <- table(train_app[,n])
    
    val_list <- which(val_list<=5) #9
    if(length(val_list)>=2){
        #     names(val_list)
#         filter <- train_app[which(train_app[,n] %in% names(val_list)),]
#         filter <- filter[which(filter$click == '1'),]
#         val_list_op <- table(filter[,n])
#         val_list_final <- names(val_list)[which(!names(val_list) %in% names(val_list_op))]
#         train_app[which(train_app[,n] %in% val_list_final),n] <- 'other'
        train_app[which(train_app[,n] %in% val_list),n] <- 'other'
        
        gc()
#         print(paste('Feature',colnames(train_app)[n],'finished.', length(val_list_final), 'features removed!'))
        print(paste('Feature',colnames(train_app)[n],'finished.', length(val_list), 'features removed!'))
    }
}

dim(train_app)
# test_app <- train_app[14596138:16315441 , -2]
test_app <- train_app[25832831:28690990 , -2]
tail(test_app);gc()
# train_app <- train_app[-c(14596138:16315441),]
train_app <- train_app[-c(25832831:28690990),]
head(train_app);gc()
dim(train_app);dim(test_app)

# names(train_app)<-c('id','click','a_hour','b_C1','c_banner_pos','d_app_id','e_app_domain','f_app_category','g_device_id','h_device_ip',
#                    'i_device_ip_2','j_device_model','k_device_type','l_device_conn_type','m_C14','n_C15','o_C16','p_C17','q_C18','r_C19',
#                    's_C20','t_C21')
# names(test_app)<-c('id','a_hour','b_C1','c_banner_pos','d_app_id','e_app_domain','f_app_category','g_device_id','h_device_ip',
#                    'i_device_ip_2','j_device_model','k_device_type','l_device_conn_type','m_C14','n_C15','o_C16','p_C17','q_C18','r_C19',
#                    's_C20','t_C21')

names(train_app)<-c('id','click','a_hour','b_C1','c_banner_pos','d_site_id','e_site_domain','f_site_category','g_device_id','h_device_ip',
                   'i_device_ip_2','j_device_model','k_device_type','l_device_conn_type','m_C14','n_C15','o_C16','p_C17','q_C18','r_C19',
                   's_C20','t_C21')
names(test_app)<-c('id','a_hour','b_C1','c_banner_pos','d_site_id','e_site_domain','f_site_category','g_device_id','h_device_ip',
                  'i_device_ip_2','j_device_model','k_device_type','l_device_conn_type','m_C14','n_C15','o_C16','p_C17','q_C18','r_C19',
                  's_C20','t_C21')
head(train_app);head(test_app);gc()

# write.csv(train_app, file = 'data/train_df_app_split_smooth.csv', quote = F, row.names = F)
# write.csv(test_app, file = 'data/test_df_app_split_smooth.csv', quote = F, row.names = F)

write.csv(train_app, file = 'data/train_df_site_split_smooth.csv', quote = F, row.names = F)
write.csv(test_app, file = 'data/test_df_site_split_smooth.csv', quote = F, row.names = F)
