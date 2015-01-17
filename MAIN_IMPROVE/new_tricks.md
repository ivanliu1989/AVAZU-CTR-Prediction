1. histogram xgboost （ensemble）


2. Model:Libfm(dim= 8 iter=70 learn_tate= 0.0001 regular= 0.005)

- dim 0,1,15 -learn_rate 0.0001 -iter 70 and around 40 mil features.

3. It is a smoothed version((#nclick+ alpha *0.25)/ (#ncount+alpha) ) of CTR(alpha=10) conditioned on each of categorical variables, so if a feature does not occur in training, the value is 0.25

4.  ngrams VW/nn VW

##### results
ngrams 2: LB:0.4026492
ngrams 3 (no interaction, l .13, no l1): 0.429678/0.291196 | LB: 0.4096855




../../libfm-1.42.src/bin/libFM -task c -train data/libsvm_train_full_site.txt -test data/libsvm_test_site.txt -out pred/libFM_pred_site_ALS_70.txt -dim '0,1,15' -iter 70 -method als -regular 0.005 -learn_rate 0.0001

