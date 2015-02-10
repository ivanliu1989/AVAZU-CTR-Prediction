VAZU-CTR-Prediction
===================

In online advertising, click-through rate (CTR) is a very important metric for evaluating ad performance. As a result, click prediction systems are essential and widely used for sponsored search and real-time bidding. 

For this competition, we have provided 11 days worth of Avazu data to build and test prediction models. Can you find a strategy that beats standard classification algorithms? The winning models from this competition will be released under an open-source license.

#### Final solution:
	1. folder: Summary / IMPROVE
	2. ranking: 55/1786


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

##### latest findings
31.10 = Halloween being qualitatively different from the rest of the sample

maybe training specifically on 24 (Friday) and/or 25-26 (weekend ~ holiday) would help?
Holdout 2 days of data for CV, just 1 gives poorer performance (around 0.006 as you mentioned above)
Split the data in one file per day
Refactor the training and validation logic so I can pass a range of days I want to train/validate on.

http://cran.at.r-project.org/web/packages/FeatureHashing/index.html

#### preprocessing
1. add columns for <b>Hour</b> , <b>Weekday</b> , <b>Public Holiday</b>
2. Hash / one-hotted
3. Split train based on different days

#### modeling
1. python fast learning
2. vw
3. xgboost
4. caret adaptive (svm)
5. solution below
6. ensembles
7. calibration (-0.000x)

#### solution
1. GBDT - feature generation
2. Hashing tricks - feature generation for FM(Factorization Machine)
3. Factorization Machine
