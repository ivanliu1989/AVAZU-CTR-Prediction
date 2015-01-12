IMPROVEMENTS BASED ON MAJOR PLANNING
===================

##### Step 1 FEATURE ENGINEERING
	- Features in test not in train
		1. First 3 digits in ID => geographical info
		2. Unseen variables => 'Other'(-2)

##### Step 2 SHUFFLE DATA

##### Step 3 VALIDATION (1.5%)

##### Step 4 SEPARATELY TUNING MODELS => Vowpal Wabbit

##### Step 5 SINGLE MODELS
	- libFM
		1. SGD
		2. MCMC
	- xgboost
		1. GBM
	- R/Python 
		1. SVM - batch (avg results)

##### Step 6 BLENDING
	- Weighted