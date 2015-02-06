	- alias vw=/Users/ivan/Work_directory/vowpal_wabbit-7.9/vowpalwabbit/vw

##### testing
	- vw sparse/test_df_site.vw -t -i sparse/model_site.vw -p avazu.preds.site.sparse.txt 
	- vw test_df_app.vw -t -i model_app.vw -p avazu.preds.app.txt
##### ftrl
	- vw -d train_df_site.vw --loss_function logistic -b 28 -c -k --passes 3 -f model_site.vw --holdout_after 17850000 --l1 1 --l2 6 --decay_learning_rate 0.8 --ftrl --ftrl_alpha 0.15 --ftrl_beta 1
	114286000
	- vw -d train_df_site.vw --loss_function logistic -b 28 -c -k --passes 3 -f model_site.vw --holdout_after 17850000 --l1 1 --l2 6 --decay_learning_rate 0.8 --ftrl --ftrl_alpha 0.15 --ftrl_beta 1 -q ki -q kj -q ij -q kl -q il -q jl -q ef -q ce -q cf -q ho

	1/6: 0.438542/0.306634 | 0.3932844
	12e-9/6e-9: 0.437691/0.304923 | 0.3935493
	alpha 0.15/beta 0.1: 0.43649/0.301758 | 0.4017696
	alpha 0.15/beta/-q/l1 1: 0.440245/0.304372 | 0.4069576
	l1-3/l2-6/beta-1/alpha-0.5: 0.438659/0.305284 | 
	l1-6/l2-14/beta-1/alpha-0.2/pair: | 
##### training
1. Non-polynomial
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.2 -c -k --passes 6 -f model_site.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8

2. Polynomial
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.2 -c -k --passes 6 -f model_site.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8 -q :: --early_terminate 1
	- vw -d train_df_app.vw --loss_function logistic -b 28 -l 0.15 -c -k --passes 6 -f model_app.vw --holdout_period 10 --l1 12e-09 --l2 6e-09 --decay_learning_rate 0.8 -q :: --early_terminate 1

3. NN
	- vw -d train_df_site.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 6 -f model_site_nn.vw --holdout_period 100 --early_terminate 2 --nn 160 --power_t 0
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

##### poly/cubic command
0.426625 | 6 passes | 0.3957190
0.287565 | 7 passes | 0.3957190

vw -d train_df_site.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_site.vw --holdout_period 100 --l1 3e-9 --l2 6e-9 --decay_learning_rate 0.9 -q sd -q cc --cubic sss --cubic ddd --early_terminate 3
0.425166 | 6 passes | 0.3975120

vw -d train_df_app.vw --loss_function logistic -b 28 -l .13 -c -k --passes 15 -f model_app.vw --holdout_period 100 --l1 3e-9 --l2 6e-9 --decay_learning_rate 0.9 -q ad -q cc --cubic aaa --cubic ddd --early_terminate 3
0.28738 | 6 passes | 0.3975120

vw -d name_space/train_df_site.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_site_nn.vw --holdout_period 100 --early_terminate 3 --nn 160 --power_t 0
0. |  passes | 0.

vw -d name_space/train_df_app.vw --loss_function logistic -b 28 -l 0.01 -c -k --passes 16 -f model_app_nn.vw --holdout_period 100 --early_terminate 3 --nn 130 --power_t 0
0. |  passes | 0.