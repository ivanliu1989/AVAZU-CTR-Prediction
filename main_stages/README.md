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


#### Predictions
##### NULL, Split, HOUR
###### fast solution python
0.1 | 1 | 4 | 4 | 28 - local: / | LB: 0.3940511  ++<br>
0.1 | 1.5 | 4 | 4 | 28 - local: 0.441747/0.310183 | LB: 0.3941666  -<br>
0.12 | 1.5 | 4 | 4 | 28 - local: 0.441551/0.309723 | LB: 0.3941158 +<br>
0.1 | 1 | 6 | 6 | 28 - local: 0.441921/0.310515 | LB: 0.3942410 -<br>
0.12 | 1.5 | 4 | 4 | 28 - local: 0.440745/0.308922 | LB: 0.3934614 (smooth)<br>
0.12 | 1.5 | 4 | 4 | 28 - local: 0.440846/0.308867 | LB: 0.3935246 (smooth - 10)<br>

###### VW
-b 28 -l 0.1 -c -k --passes 3 --holdout_period 100 | local: / | LB: 0.3939303 <br>
-b 28 -l 0.12 -c -k --passes 3 --holdout_period 100 | local: 0.437666/0.300353 | LB: 0.3938035 ++<br>
-b 28 -l 0.12 -c -k --passes 3 --holdout_period 100 | local: 0.438099/0.301331 | LB: 0.3933600 (smooth)<br>

