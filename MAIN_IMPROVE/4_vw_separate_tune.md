	- alias vw=/Users/ivan/Work_directory/vowpal_wabbit-7.9/vowpalwabbit/vw

##### testing
	- vw test_df_site.vw -t -i model_site.vw -p avazu.preds.site.txt 
	- vw test_df_app.vw -t -i model_app.vw -p avazu.preds.app.txt

##### training
1. Non-polynomial
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.2 -c -k --passes 6 -f model_site.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8

2. Polynomial
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.2 -c -k --passes 6 -f model_site.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8 -q :: --early_terminate 1
	- vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 6 -f model_app.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8 -q :: --early_terminate 1

3. NN
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 6 -f model_site_nn.vw --holdout_period 100 --early_terminate 2 --nn 130 --power_t 0
	- vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 6 -f model_app_nn.vw --holdout_period 100 --early_terminate 2 --nn 130 --power_t 0

##### Old
-b 28 -l 0.12 -c -k --passes 3 --holdout_period 100 | local: 0.438099/0.301331 | LB: 0.3933600 (smooth)<br>
	-(0.2/0.9)0.43565/0.296655 |lb: 0.3946054
	-(0.13) 0.437381/0.299485 | lb: 0.3938755


0.13 | 1 | 1 | 1 | 28 - local: 0.439512/0.306498 | LB: 0.3931091 (smooth - 5)<br>
0.2 | 1 | 1 | 1 | 28 - local: / | LB: <br>

##### calibration
ctr - 0.16980562476404604 <br>
ctr-test - 0.17470822297322214 <br>
calibration - -0.004902598209176101 <br>
LB: 0.3903022

##### poly/nominal ensemble
	- 0.3931037
	- 0.3979055
	- 0.3926943

##### poly command
vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 6 -f model_site.vw --holdout_period 100 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.9 -q :: --early_terminate 2 --bfgs --ftrl --ftrl_alpha 0.1 --ftrl_beta 0
vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 6 -f model_app.vw --holdout_period 100 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.9 -q :: --early_terminate 2 --bfgs --ftrl --ftrl_alpha 0.1 --ftrl_beta 0

vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 6 -f model_site.vw --holdout_period 100 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.9 --cubic ::: --early_terminate 2 --bfgs --ftrl --ftrl_alpha 0.1 --ftrl_beta 0
vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 6 -f model_app.vw --holdout_period 100 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.9 --cubic ::: --early_terminate 2 --bfgs --ftrl --ftrl_alpha 0.1 --ftrl_beta 0
