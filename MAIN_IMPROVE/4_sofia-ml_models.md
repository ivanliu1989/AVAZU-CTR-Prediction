###### https://code.google.com/p/sofia-ml/

##### Test the code:
	
	# Train a model on the demo training data.
	./sofia-ml --learner_type pegasos --loop_type stochastic --lambda 0.1 --iterations 100000 --dimensionality 150000 --training_file demo/demo.train --model_out demo/model

   	# Test the model on the demo data.
   	./sofia-ml --model_in demo/model --test_file demo/demo.train --results_file demo/results.txt

	# Examine a few results in the results file:
	head -5 demo/results.txt

	# Evaluate the results:
	perl eval.pl demo/results.txt
	
##### Training Commands:
	../../sofia-ml-read-only/sofia-ml --learner_type pegasos --loop_type stochastic --lambda 0.1 --iterations 100000 --dimensionality 2^28 --training_file data/sofia_train_app.txt --model_out model/sofia_app_model

	../../sofia-ml-read-only/sofia-ml --model_in model/sofia_app_model --test_file data/sofia_test_app.txt --results_file pred/sofia_pred_app.txt --prediction_type logistic

	../../sofia-ml-read-only/sofia-ml --learner_type pegasos --loop_type stochastic --lambda 0.1 --iterations 100000 --dimensionality 2^28 --training_file data/sofia_train_site.txt --model_out model/sofia_site_model

	../../sofia-ml-read-only/sofia-ml --model_in model/sofia_site_model --test_file data/sofia_test_site.txt --results_file pred/sofia_pred_site.txt --prediction_type logistic

##### Algorithms options
	--learner_type (pegasos, sgd-svm, logreg-pegasos)
	--loop_type (stochastic, balanced-stochastic, rank, )

##### Others
	--passive_aggressive_c float
	Maximum size of any step taken in a single passive-aggressive update.

	--passive_aggressive_lambda float
	Lambda for pegasos-style projection for passive-aggressive update. When set to 0 (default) no projection is performed.

	--perceptron_margin_size float
	Width of margin for perceptron with margins. Default of 1 is equivalent to unregularized SVM-loss.

	--rank_step_probability float
	Probability that we will take a rank step (as opposed to a standard stochastic gradient step) in a combined-ranking or combined-roc loop.
	Default: 0.5

	--hash_mask_bits int
	When set to a non-zero value, causes the use of a hashed weight vector with hashed cross product features.
	This allows learning on conjunction of features, at some increase in computational cost.
	Note that this flag must be set both in training and testing to function properly.
	The size of the hash table is set to 2^--hash_mask_bits.
	Default value of 0 shows that hash cross products are not used.
