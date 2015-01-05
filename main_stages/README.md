Major Planning
===================

##### Step 1 Preprocessing-A
Feature Engineering, generate features for GBDT<br>
	- DOW, Hour, Holiday<br>
	- One-hot encoding<br>
	- Summary<br>

##### Step 2 Gradient Boosting Decision Tree
xgboost<br>
	- 30 trees with depth 7<br>
	- features generation<br>

##### Step 3 Preprocessing-B
Fenerate features for FM<br>
	- Numerical features greater than 2 are transformed by v ← log(v)2<br>
	- GBDT features are directly included<br>
	- hashing trick<br>
Each impression has XX(numerical) + XX(categorical) + XX(GBDT) = XX features<br>

##### Step 4 Factorization Machine
libFM<br>

##### Step 5 Calibration
There is a gap. So minus every prediction by 0.003.<br>