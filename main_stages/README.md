Major Planning
===================

##### Step 1 Preprocessing-A
Feature Engineering, generate features for GBDT<br>
	- Hour (DOW, Hour)<br>
	- Noisy removal, <= 5 freq<br>
	- One-hot encoding(factor() | sparse.model.matrix())<br>
	- Split by day, app, site (option)<br>

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
	- App, Site<br>
	- GBDT feature

##### Step 6 Calibration
There is a gap. So minus every prediction by 0.003.<br>