##### 1. MCMC
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_app_full.txt -test libsvm_test_app.txt -out libFM_pred_app_MCMC.txt -dim ’1,1,8’ -iter 10 -method mcmc -init_stdev 0.1
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_site_full.txt -test libsvm_test_site.txt -out libFM_pred_site_MCMC.txt -dim ’1,1,8’ -iter 10 -method mcmc -init_stdev 0.1

##### 2. ALS
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_app_full.txt -test libsvm_test_app.txt -out libFM_pred_app_ALS.txt -dim ’1,1,8’ -iter 10 -method als -regular ’0,0,10’ -init_stdev 0.1
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_site_full.txt -test libsvm_test_site.txt -out libFM_pred_site_ALS.txt -dim ’1,1,8’ -iter 10 -method als -regular ’0,0,10’ -init_stdev 0.1

##### 3. SGD
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_app_full.txt -test libsvm_test_app.txt -out libFM_pred_app_SGD.txt -dim ’1,1,8’ -iter 10 -method sgd -learn_rate 0.01 -regular ’0,0,0.01’ -init_stdev 0.1
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_site_full.txt -test libsvm_test_site.txt -out libFM_pred_site_SGD.txt -dim ’1,1,8’ -iter 10 -method sgd -learn_rate 0.01 -regular ’0,0,0.01’ -init_stdev 0.1

##### 4. SGDA
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_app.txt -test libsvm_test_app.txt -out libFM_pred_app_SGDA.txt -dim ’1,1,8’ -iter 10 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation libsvm_validation_app.txt
../../libfm-1.42.src/bin/libFM -task c -train libsvm_train_site.txt -test libsvm_test_site.txt -out libFM_pred_site_SGDA.txt -dim ’1,1,8’ -iter 10 -method sgda -learn_rate 0.01 -init_stdev 0.1 -validation libsvm_validation_site.txt