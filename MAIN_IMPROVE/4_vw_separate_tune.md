	- alias vw=/Users/ivan/Work_directory/vowpal_wabbit/vowpalwabbit/vw

##### testing
	- vw test_df_site.vw -t -i model_site.vw -p avazu.preds.site.txt 
	- vw test_df_app.vw -t -i model_app.vw -p avazu.preds.app.txt

##### training
1. Non-polynomial
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.2 -c -k --passes 6 -f model_site.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8

2. Polynomial
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.2 -c -k --passes 6 -f model_site.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8 -q :: 
	- vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.2 -c -k --passes 6 -f model_app.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8 -q ::

3. NN
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 3 -f model_site.vw --holdout_period 10 --termination 0.001 --nn 20 -q :: --power_t 0

