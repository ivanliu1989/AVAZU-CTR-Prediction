#####VW:
alias vw=/Users/ivan/Work_directory/vowpal_wabbit/vowpalwabbit/vw <br>
alias vw-hypersearch=/Users/ivan/Work_directory/vowpal_wabbit/utl/vw-hypersearch <br>

vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.12 -c -k --passes 3 -f model_site.vw --holdout_period 100 <br>
vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.12 -c -k --passes 3 -f model_app.vw --holdout_period 100 <br>

vw test_df_site.vw -t -i model_site.vw -p avazu.preds.site.txt <br>
vw test_df_app.vw -t -i model_app.vw -p avazu.preds.app.txt <br>

vw-hypersearch 0.05 0.15 vw -d train_df_site.vw --loss_function logistic -b 28 -l % -c -k --passes 3 -f model_site.vw --holdout_period 100 <br>
vw-hypersearch 0.05 0.15 vw -d train_df_app.vw --loss_function logistic -b 28 -l % -c -k --passes 3 -f model_app.vw --holdout_period 100 <br>


#####xgboost:
../../xgboost-master/xgboost Step_2.1_xgboost_app.conf <br>
../../xgboost-master/xgboost Step_2.1_xgboost_app.conf task=pred model_in=model/model_app.model <br>
../../xgboost-master/xgboost Step_2.1_xgboost_app.conf task=eval eval[name]=data/libsvm_train_app.txt model_in=model/model_app.model <br>


#####FM
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_app.txt -test libsvm_test_app.txt -dim '1,1,8' -out libFM_pred_app.txt -verbosity 1 -method mcmc -init_stdev 0.1 -iter 100 <br>
-method SGD, SGDA, ALS, MCMC <br>
-learn_rate 0.1 <br>
-regular 'r0,r1,r2'

#####VW improve:
1. Shuffle the data before making the model as the VW algorithm is an online learner and might have given more preference to the latest data
2. provide high weights for clicks as data is skewed. How Much? 
3. tune VW algorithm using vw-hypersearch. What should be tuned?
4. Use categorical features like |C1 "C1"&"1"