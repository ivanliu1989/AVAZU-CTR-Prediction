	- alias vw=/Users/ivan/Work_directory/vowpal_wabbit-7.9/vowpalwabbit/vw
	- alias vw-hypersearch=/Users/ivan/Work_directory/vowpal_wabbit-7.9/utl/vw-hypersearch

	- vw sparse/test_df_site.vw -t -i sparse/model_site.vw -p avazu.preds.site.sparse.txt --link logistic
#### Tips for Vowpal wabbit
	1. 2-grams on ALL the features. (VW)
	2. Neural networks. (VW)
	3. All loss functions (logistic loss, hinge loss, squared loss, quantile loss) (VW)
	4. Nearest neighbours (libSVM)
	5. Factorization machines. (libFM)
	6. SVC (libSVM)

#### Vowpal wabbit cubic [4]
	vw -d train_df_site.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_site.vw --holdout_period 100 --l2 6e-9 --decay_learning_rate 0.9 -q sd -q cc --cubic sss --cubic ddd --early_terminate 3

	vw -d train_df_app.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_app.vw --holdout_period 100 --l1 3e-9 --l2 6e-9 --decay_learning_rate 0.9 -q ad -q cc --cubic aaa --cubic ddd --early_terminate 3

	0.425166/0.28738 | 0.3975120


#### Vowpal wabbit Name_space 
	vw -d name_space/train_df_site.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 15 -f name_space/model_site.vw --holdout_period 100 --decay_learning_rate 0.9 --early_terminate 3 --l2 6e-8 --bootstrap 10

	vw-hypersearch -l 0.01 0.3 vw --loss_function logistic -l % name_space/train_df_app.vw
	
	0.43852/0.30065 | lb: 0.3938007
	0.442204/0.307986 | bootstrap lb: 0.3977472


#### Vowpal wabbit NN [2]
	vw -d name_space/train_df_site.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_site_nn.vw --holdout_period 100 --early_terminate 3 --nn 38 --power_t 0

	vw -d name_space/train_df_app.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_app_nn.vw --holdout_period 100 --early_terminate 3 --nn 38 --power_t 0

	0.431702/0.293282 | 0.4073284/0.3987734


#### Vowpal wabbit SVM [3]
	vw -d train_df_app.vw --ksvm --kernel linear -b 28 -c -k -f svm/model_app.vw --l2 6e-9 --passes 3 --reprocess 2 --loss_function logistic --link logistic

	linear, poly(--degree 2), rbf(--bandwidth 1)

	vw sparse/test_df_site.vw -t -i sparse/model_site.vw -p avazu.preds.site.sparse.txt --link logistic


#### LibFM MCMC [5]
	../../libfm-1.42.src/bin/libFM -task c -train data/libsvm_train_full_app.txt -test data/libsvm_test_app.txt -out libFM_pred_app_MCMC_900.txt -dim ’1,1,8’ -iter 900 -method mcmc -init_stdev 0.1

	../../libfm-1.42.src/bin/libFM -task c -train data/libsvm_train_full_site.txt -test data/libsvm_test_site.txt -out pred/libFM_pred_site_MCMC_70.txt -dim '0,1,15' -iter 70 -method mcmc -regular 0.005 -learn_rate 0.1

#### LibLinear [5]
	../../liblinear-1.96/train -s 7 -c 1 -v 10 -e 0.001 data/sofia_train_app.txt model/libLinear_app_model.model
	../../liblinear-1.96/predict -b 1 data/sofia_test_app.txt model/libLinear_app_model.model pred/liblinear_pred_app

	../../liblinear-1.96/train -s 7 -c 1 -v 10 -e 0.001 data/sofia_train_site.txt model/libLinear_site_model.model
	../../liblinear-1.96/predict -b 1 data/sofia_test_site.txt model/libLinear_site_model.model pred/liblinear_pred_site


#### Xgboost ensemble [6]
	../../xgboost-master/xgboost 4_xgboost_app.conf
	../../xgboost-master/xgboost 4_xgboost_app.conf task=pred

	../../xgboost-master/xgboost 4_xgboost_site.conf
	../../xgboost-master/xgboost 4_xgboost_site.conf task=pred

	eta = 0.6 | gamma = 0.1 | max_depth = 9 | num_round = 100 | subsample = 0.7squared

#### Model List
	1. vw logistic + | 0.3931037
	2. vw nn + | 0.3987734
	3. vw cubic + | 0.3957190
	4. libFM MCMC + | 0.4027643
	5. xgboost 0.7*9 + | 0.3931970
	6. libLinear - | 

