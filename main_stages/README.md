Major Planning
===================

##### Step 1 Preprocessing-A
Feature Engineering, generate features for GBDT<br>
	- DOW, Hour<br>
	- Noisy removal<br>
	- One-hot encoding(factor() | sparse.model.matrix())<br>
	- Summary<br>

##### Step 2 Gradient Boosting Decision Tree
xgboost<br>
	- 20 trees with depth 7<br>
	- features generation<br>

##### Step 3 Preprocessing-B
Fenerate features for FM<br>
	- Numerical features greater than 2 are transformed by v ← log(v)2<br>
	- GBDT features are directly included<br>
	- hashing trick<br>
Each impression has 25(categorical) + 20(GBDT) = 45 features<br>

##### Step 4 Factorization Machine
libFM<br>

##### Step 5 Calibration
There is a gap. So minus every prediction by 0.003.<br>