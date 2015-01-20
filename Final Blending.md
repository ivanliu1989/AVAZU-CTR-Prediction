	- alias vw=/Users/ivan/Work_directory/vowpal_wabbit-7.9/vowpalwabbit/vw
	- alias vw-hypersearch=/Users/ivan/Work_directory/vowpal_wabbit-7.9/utl/vw-hypersearch

	- vw sparse/test_df_site.vw -t -i sparse/model_site.vw -p avazu.preds.site.sparse.txt
#### Tips for Vowpal wabbit
	1. 2-grams on ALL the features. 
	2. Neural networks.
	3. All loss functions (logistic loss, hinge loss, squared loss, quantile loss)
	4. Nearest neighbours
	5. Factorization machines. 
	6. SVC
	7. 
#### Vowpal wabbit cubic [4]
	vw -d train_df_site.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_site.vw --holdout_period 100 --l2 6e-9 --decay_learning_rate 0.9 -q sd -q cc --cubic sss --cubic ddd --early_terminate 3

	vw -d train_df_app.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_app.vw --holdout_period 100 --l1 3e-9 --l2 6e-9 --decay_learning_rate 0.9 -q ad -q cc --cubic aaa --cubic ddd --early_terminate 3

	0.425166/0.28738 | 0.3975120

#### Vowpal wabbit Name_space | Sparse (LBFGS) [1]
	vw -d name_space/train_df_site.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 15 -f name_space/model_site.vw --holdout_period 100 --decay_learning_rate 0.9 --early_terminate 3 --termination 0.001 --mem 15 --l2 0.0 --bfgs

	vw -d sparse/train_df_site.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 15 -f sparse/model_site.vw --holdout_period 100 --decay_learning_rate 0.9 --early_terminate 3 --l2 6e-8

	vw-hypersearch -l 0.01 0.3 vw --loss_function logistic -l % name_space/train_df_app.vw
	
	0.43852/0.30065 | lb: 0.3938007
	0.438522/0.300654 |

#### Vowpal wabbit NN [2]
	vw -d name_space/train_df_site.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_site_nn.vw --holdout_period 100 --early_terminate 3 --nn 38 --power_t 0

	vw -d name_space/train_df_app.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_app_nn.vw --holdout_period 100 --early_terminate 3 --nn 38 --power_t 0


#### Vowpal wabbit Hinge [3]
	vw -d name_space/train_df_site.vw --loss_function hinge -b 28 -l 0.15 -c -k --passes 15 -f name_space/model_site.vw --holdout_period 100 --decay_learning_rate 0.9 --early_terminate 3 --l2 6e-8

	vw -d name_space/train_df_app.vw --loss_function hinge -b 28 -l 0.15 -c -k --passes 15 -f name_space/model_app.vw --holdout_period 100 --decay_learning_rate 0.9 --early_terminate 3 --l2 6e-8


#### LibFM MCMC [5]
	../../libfm-1.42.src/bin/libFM -task c -train data/libsvm_train_full_app.txt -test data/libsvm_test_app.txt -out libFM_pred_app_MCMC_900.txt -dim ’1,1,8’ -iter 900 -method mcmc -init_stdev 0.1

	../../libfm-1.42.src/bin/libFM -task c -train data/libsvm_train_full_site.txt -test data/libsvm_test_site.txt -out pred/libFM_pred_site_MCMC_70.txt -dim '0,1,15' -iter 70 -method mcmc -regular 0.005 -learn_rate 0.0001


#### Sofia-ML (libSVM) [6]
	../../sofia-ml-read-only/sofia-ml --learner_type logreg-pegasos --loop_type stochastic --lambda 0.000001 --iterations 80000000 --dimensionality 845000 --training_file data/sofia_train_app.txt --model_out model/sofia_app_model

	../../sofia-ml-read-only/sofia-ml --model_in model/sofia_app_model --test_file data/sofia_test_app.txt --results_file pred/sofia_pred_app.txt --prediction_type logistic

	--loop_type (roc, stochastic)


#### Xgboost ensemble [6]
	../../xgboost-master/xgboost 4_xgboost_app.conf
	../../xgboost-master/xgboost 4_xgboost_app.conf task=pred

	../../xgboost-master/xgboost 4_xgboost_site.conf
	../../xgboost-master/xgboost 4_xgboost_site.conf task=pred

	eta = 0.6 | gamma = 0.1 | max_depth = 9 | num_round = 100 | subsample = 0.7
