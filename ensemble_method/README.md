Ensemble modeling
===================

##### meta data and different hyperparameters
	- xgboost (learning rate, depth ...)
	- FM (k, stopping, learning rate, regularization) (SGD, MCMC)
	- add results as predictors in ensemble models
	- average results from different models

##### xgboost
	- subsample = 0.75 | eta = (0.1,0.3,0.9) | max_depth = (6,9) | num_round = (50,100,150) | seed = (8,88,888,8888)

##### fm
	- dim '1,1,8' | method (mcmc,SGD) | learn_rate (0.1,0.15,0.2) | regular (1,3,6)