Major Planning
===================

##### Step 1 Preprocessing-A
Feature Engineering, generate features for GBDT
	- DOW, Hour, Holiday
	- One-hot encoding
	- Summary

##### Step 2 Gradient Boosting Decision Tree
xgboost
	- 30 trees with depth 7
	- features generation

##### Step 3 Preprocessing-B
Fenerate features for FM
	- Numerical features greater than 2 are transformed by v ← log(v)2
	- GBDT features are directly included
	- hashing trick
Each impression has XX(numerical) + XX(categorical) + XX(GBDT) = XX features

##### Step 4 Factorization Machine
libFM

##### Step 5 Calibration
There is a gap. So minus every prediction by 0.003.