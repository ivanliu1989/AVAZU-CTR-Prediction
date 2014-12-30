pypy csv_to_vw.py

vw train.vw -f avazu.model.vw --loss_function logistic

vw test.vw -t -i avazu.model.vw -p avazu.preds.txt

pypy vw_to_kaggle.py
