Major Planning
===================

##### Step 1 Preprocessing-A
Feature Engineering, generate features for GBDT<br>
	- Hour (DOW, Hour)<br>
	- Noisy removal, <= 5 freq | laplace smooth<br>
	- Null value [d41d8cd9,85f751fd,c4e18dd6,50e219e0,ecad2386,7801e8d9,07d7df22]
	- Value appeared in training doesn't appear in testing
	- One-hot encoding(factor() | sparse.model.matrix() | caret dummy)<br>
	- Split mobile apps vs. sites<br>
In those columns, replace d41d8cd9 with NULL. You'll see the ad was either served on a site or an app.<br>

##### Step 2 Gradient Boosting Decision Tree
xgboost<br>
	- 20 trees with depth 7<br>
	- features generation<br>

##### Step 3 Preprocessing-B
Fenerate features for FM<br>
	- GBDT features are directly included<br>
	- hashing trick<br>
Each impression has 23(categorical) + 20(GBDT) = 43 features<br>

##### Step 4 Factorization Machine
libFM<br>

##### Step 5 Ensemble
	- App, Site <br>
	- GBDT feature <br>
blend two logistic model with different learning rate and got 0.0003 LB improvement

##### Step 6 Calibration
There is a gap. So minus every prediction by 0.003.<br>

##### Shuffle data
pypy shuffle_ooc.py train_df_app_smooth.csv > train_df_app_smooth_shuffled.csv
pypy shuffle_ooc.py train_df_site_smooth.csv > train_df_site_smooth_shuffled.csv


#### Predictions
##### NULL, Split, HOUR
###### fast solution python
0.1 | 1 | 4 | 4 | 28 - local: / | LB: 0.3940511  ++<br>
0.1 | 1.5 | 4 | 4 | 28 - local: 0.441747/0.310183 | LB: 0.3941666  -<br>
0.12 | 1.5 | 4 | 4 | 28 - local: 0.441551/0.309723 | LB: 0.3941158 +<br>
0.1 | 1 | 6 | 6 | 28 - local: 0.441921/0.310515 | LB: 0.3942410 -<br>
0.12 | 1.5 | 4 | 4 | 28 - local: 0.440745/0.308922 | LB: 0.3934614 ++ (smooth) 0.440745 | 0.308922<br> 
0.12 | 1.5 | 4 | 4 | 28 - local: 0.440846/0.308867 | LB: 0.3935246 (smooth - 10)<br>
* 0.12 | 1 | 3 | 6 | 28 - local: 0.440523/0.308454 | LB:  (smooth - 5)<br>
* 0.13 | 1 | 3 | 6 | 28 - local: 0.440446/0.308270 | LB:  (smooth - 5)<br>
* 0.13 | 1 | 2 | 6 | 28 - local: 0.440191/0.307800 | LB:  (smooth - 5)<br>
* 0.13 | 1 | 1 | 6 | 28 - local: 0.439785/0.307126 | LB:  (smooth - 5)<br>
* 0.13 | 1 | 1 | 1 | 28 - local: 0.439512/0.306498 | LB: 0.3931091 (smooth - 5)<br>
0.14 | 1 | 1 | 1 | 28 - local: 0.439405/0.306257 | LB: 0.3931330 (smooth - 5)<br>
0.13 | 1 | 1 | 3 | 28 - local: 0.439631/0.306774 | LB: 0.3931350  (smooth - 5)<br>
0.13 | 1 | 1 | 1 | 28 - local: 0.441814/0.315843 | LB: 0. (smooth - 5 | without ID)<br>
0.3931330 & 0.4012691 ensemble | LB: 0.3930214 (smooth - 5)<br>

0.2 | 1 | 1 | 4 | 28 - local: 0.305771

###### VW
-b 28 -l 0.1 -c -k --passes 3 --holdout_period 100 | local: / | LB: 0.3939303 <br>
-b 28 -l 0.12 -c -k --passes 3 --holdout_period 100 | local: 0.437666/0.300353 | LB: 0.3938035 ++<br>
-b 28 -l 0.12 -c -k --passes 3 --holdout_period 100 | local: 0.438099/0.301331 | LB: 0.3933600 (smooth)<br>

###### xgboost
eta = 1 | gamma = 0.3 | max_depth = 8 | num_round = 2 | LB: 0.4103132 <br>
eta = 0.8 | gamma = 0.1 | max_depth = 16 | num_round = 8 | LB: 0.3999703 <br>
eta = 0.8 | gamma = 0.1 | max_depth = 16 | num_round = 2 | LB: 0.4102534 <br>
eta = 1 | gamma = 0.1 | max_depth = 16 | num_round = 2 | LB: 0.4052225 <br>
eta = 1 | gamma = 0.3 | max_depth = 16 | num_round = 2 | LB: 0.4052255 <br>
eta = 1 | gamma = 0.3 | max_depth = 20 | num_round = 2 | LB: 0.4046538 <br>
ensemble 4 | LB: 0.4051936 <br>
eta = 0.3 | gamma = 0.1 | max_depth = 8 | num_round = 50 | LB: 0.4012691 <br>


../../xgboost-master/xgboost Step_2.1_xgboost_app.conf
../../xgboost-master/xgboost Step_2.1_xgboost_app.conf task=pred model_in=model/model_app.model
