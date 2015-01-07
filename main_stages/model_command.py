alias vw=/Users/ivan/Work_directory/vowpal_wabbit/vowpalwabbit/vw

vw -d train_df.vw --loss_function logistic -b 28 -l 0.1 -c -k --passes 3 -f model_holdout.vw --holdout_period 100

vw test_df.vw -t -i model_holdout.vw -p avazu.preds.txt


../../xgboost-master/xgboost Step_2.1_xgboost.conf

../../xgboost-master/xgboost Step_2.1_xgboost.conf task=pred model_in=0003.model

../../xgboost-master/xgboost Step_2.1_xgboost.conf task=dump model_in=0003.model name_dump=dump.raw.txt 
../../xgboost-master/xgboost Step_2.1_xgboost.conf task=dump model_in=0003.model fmap=featmap.txt name_dump=dump.nice.txt

../../xgboost-master/xgboost Step_2.1_xgboost.conf model_in=0002.model num_round=2 model_out=continue.model

id,hour,C1,banner_pos,site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21,dow
id,click,hour,C1,banner_pos,site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model,device_type,device_conn_type,C14,C15,C16,C17,C18,C19,C20,C21,dow