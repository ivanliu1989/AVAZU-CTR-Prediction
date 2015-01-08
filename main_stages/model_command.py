alias vw=/Users/ivan/Work_directory/vowpal_wabbit/vowpalwabbit/vw

vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.1 -c -k --passes 3 -f model_site.vw --holdout_period 100
vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.1 -c -k --passes 3 -f model_app.vw --holdout_period 100

vw test_df_site.vw -t -i model_site.vw -p avazu.preds.site.txt
vw test_df_app.vw -t -i model_app.vw -p avazu.preds.app.txt


../../xgboost-master/xgboost Step_2.1_xgboost.conf

../../xgboost-master/xgboost Step_2.1_xgboost.conf task=pred model_in=0003.model

../../xgboost-master/xgboost Step_2.1_xgboost.conf task=dump model_in=0003.model name_dump=dump.raw.txt 
../../xgboost-master/xgboost Step_2.1_xgboost.conf task=dump model_in=0003.model fmap=featmap.txt name_dump=dump.nice.txt

../../xgboost-master/xgboost Step_2.1_xgboost.conf model_in=0002.model num_round=2 model_out=continue.model


../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_n.txt -test libsvm_test_n.txt -dim '1,1,8' -out libFM_pred.txt -verbosity 1 -method mcmc -init_stdev 0.1 -iter 1000