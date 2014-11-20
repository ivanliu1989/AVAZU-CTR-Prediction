VAZU-CTR-Prediction
===================

In online advertising, click-through rate (CTR) is a very important metric for evaluating ad performance. As a result, click prediction systems are essential and widely used for sponsored search and real-time bidding. 

For this competition, we have provided 11 days worth of Avazu data to build and test prediction models. Can you find a strategy that beats standard classification algorithms? The winning models from this competition will be released under an open-source license.

#### Tips:
1. hour: 14-10-21-00 ~ 14-10-30-23 => hour, date => night, day, holiday, weekday
2. unpreprocessed benchmark random forest
3. feature engineering
	- one-hotted (num, less than 10k distinct value) 
	- hash (cate) 
	- feature interaction 
	- categorical less than 10 times transformation
	- long tail feature log-transformation
4. python fast learning (gradient decent)
5. xgboost (gradient boosting)
6. vw online learning (log-loss)
7. L1, L2 tuning
8. meta data
9. ensemble models

##### p.s.
alpha=.15
beta=1.1
L1=1.1
L2=1.1
D=2**22
LB score: 0.3992365

alpha=.1
beta=1.
L1=1.
L2=1.
D=2**20 (24)
LB score: 0.392 (0.3977417)