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

##### Old
-b 28 -l 0.12 -c -k --passes 3 --holdout_period 100 | local: 0.438099/0.301331 | LB: 0.3933600 (smooth)<br>
(0.2)0.438435/
(0.15)0.439258/

##### calibration
ctr - 0.16980562476404604 <br>
ctr-test - 0.17470822297322214 <br>
calibration - -0.004902598209176101 <br>
