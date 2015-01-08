Major Planning
===================

##### Step 1 Preprocessing-A
Feature Engineering, generate features for GBDT<br>
	- Hour (DOW, Hour)<br>
	- Noisy removal, <= 5 freq<br>
	- Null value [d41d8cd9,85f751fd,c4e18dd6,50e219e0,ecad2386,7801e8d9,07d7df22]
	- One-hot encoding(factor() | sparse.model.matrix())<br>
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
	- GBDT feature

##### Step 6 Calibration
There is a gap. So minus every prediction by 0.003.<br>