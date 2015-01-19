#### Vowpal wabbit cubic
	vw -d train_df_site.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_site.vw --holdout_period 100 --l1 3e-9 --l2 6e-9 --decay_learning_rate 0.9 -q sd -q cc --cubic sss --cubic ddd --early_terminate 3

	vw -d train_df_app.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_app.vw --holdout_period 100 --l1 3e-9 --l2 6e-9 --decay_learning_rate 0.9 -q ad -q cc --cubic aaa --cubic ddd --early_terminate 3


#### Vowpal wabbit NN
	vw -d name_space/train_df_site.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_site_nn.vw --holdout_period 100 --early_terminate 3 --nn 160 --power_t 0

	vw -d name_space/train_df_app.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_app_nn.vw --holdout_period 100 --early_terminate 3 --nn 130 --power_t 0


#### LibFM MCMC
	../../libfm-1.42.src/bin/libFM -task c -train data/libsvm_train_full_app.txt -test data/libsvm_test_app.txt -out libFM_pred_app_MCMC_900.txt -dim ’1,1,8’ -iter 900 -method mcmc -init_stdev 0.1

	../../libfm-1.42.src/bin/libFM -task c -train data/libsvm_train_full_site.txt -test data/libsvm_test_site.txt -out pred/libFM_pred_site_MCMC_70.txt -dim '0,1,15' -iter 70 -method mcmc -regular 0.005 -learn_rate 0.0001


#### Sofia-ML (libSVM)
	../../sofia-ml-read-only/sofia-ml --learner_type logreg-pegasos --loop_type stochastic --lambda 0.000001 --iterations 80000000 --dimensionality 845000 --training_file data/sofia_train_app.txt --model_out model/sofia_app_model

	../../sofia-ml-read-only/sofia-ml --model_in model/sofia_app_model --test_file data/sofia_test_app.txt --results_file pred/sofia_pred_app.txt --prediction_type logistic

	--loop_type (roc, stochastic)


#### Xgboost ensemble
	../../xgboost-master/xgboost 4_xgboost_app.conf
	../../xgboost-master/xgboost 4_xgboost_app.conf task=pred

	../../xgboost-master/xgboost 4_xgboost_site.conf
	../../xgboost-master/xgboost 4_xgboost_site.conf task=pred

	eta = 0.6 | gamma = 0.1 | max_depth = 9 | num_round = 100 | subsample = 0.7
