# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 09:19:02 2015

@author: Ivan.Liuyanfeng
"""
from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt

# A, paths
train_site_0 = 'data/train_df_site_smooth_conn_0.csv'               # path to training file
test_site_0 = 'data/test_df_site_smooth_conn_0.csv'                 # path to testing file
train_site_2 = 'data/train_df_site_smooth_conn_2.csv'               # path to training file
test_site_2 = 'data/test_df_site_smooth_conn_2.csv'                 # path to testing file

train_app_0 = 'data/train_df_app_smooth_conn_0.csv'               # path to training file
test_app_0 = 'data/test_df_app_smooth_conn_0.csv'                 # path to testing file
train_app_2 = 'data/train_df_app_smooth_conn_2.csv'               # path to training file
test_app_2 = 'data/test_df_app_smooth_conn_2.csv'                 # path to testing file
train_app_3 = 'data/train_df_app_smooth_conn_3.csv'               # path to training file
test_app_3 = 'data/test_df_app_smooth_conn_3.csv'                 # path to testing file
train_app_5 = 'data/train_df_app_smooth_conn_5.csv'               # path to training file
test_app_5 = 'data/test_df_app_smooth_conn_5.csv'                 # path to testing file

submission = 'submit_0_2_3_5.csv'  # path of to be outputted submission file

# B, model
alpha_site = 0.13  # learning rate
beta_site = 1   # smoothing parameter for adaptive learning rate
L1_site = 1     # L1 regularization, larger value means more regularized
L2_site = 1     # L2 regularization, larger value means more regularized

alpha_app = 0.13  # learning rate
beta_app = 1   # smoothing parameter for adaptive learning rate
L1_app = 1     # L1 regularization, larger value means more regularized
L2_app = 1     # L2 regularization, larger value means more regularized

# C, feature/hash trick
D = 2 ** 29             # number of weights to use
interaction_app = False     # whether to enable poly2 feature interactions
interaction_site = False     # whether to enable poly2 feature interactions

# D, training/validation
epoch = 1       # learn training data for N passes
holdafter = None #28   # data after date N (exclusive) are used as validation
holdout = 10000 #None  # use every N training instance for holdout validation


##############################################################################
# class, function, generator definitions #####################################
##############################################################################
class ftrl_proximal(object):
    
    def __init__(self, alpha, beta, L1, L2, D, interaction):
        # parameters
        self.alpha = alpha
        self.beta = beta
        self.L1 = L1
        self.L2 = L2

        # feature related parameters
        self.D = D
        self.interaction = interaction

        self.n = [0.] * D
        self.z = [0.] * D
        self.w = {}

    def _indices(self, x):
        # first yield index of the bias term
        yield 0

        # then yield the normal indices
        for index in x:
            yield index

        # now yield interactions (if applicable)
        if self.interaction:
            D = self.D
            L = len(x)

            x = sorted(x)
            for i in xrange(L):
                for j in xrange(i+1, L):
                    # one-hot encode interactions with hash trick
                    yield hash(str(x[i]) + '_' + str(x[j])) % D

    def predict(self, x):

        # parameters
        alpha = self.alpha
        beta = self.beta
        L1 = self.L1
        L2 = self.L2

        # model
        n = self.n
        z = self.z
        w = {}

        # wTx is the inner product of w and x
        wTx = 0.
        for i in self._indices(x):
            sign = -1. if z[i] < 0 else 1.  
            
            if sign * z[i] <= L1:
                # w[i] vanishes due to L1 regularization
                w[i] = 0.
            else:
                # apply prediction time L1, L2 regularization to z and get w
                w[i] = (sign * L1 - z[i]) / ((beta + sqrt(n[i])) / alpha + L2)

            wTx += w[i]

        # cache the current w for update stage
        self.w = w

        # bounded sigmoid function, this is the probability estimation
        return 1. / (1. + exp(-max(min(wTx, 35.), -35.)))

    def update(self, x, p, y):
        
        # parameter
        alpha = self.alpha

        # model
        n = self.n
        z = self.z
        w = self.w
        # gradient under logloss
        g = p - y

        for i in self._indices(x):
            sigma = (sqrt(n[i] + g * g) - sqrt(n[i])) / alpha
            z[i] += g - sigma * w[i]
            n[i] += g * g


def logloss(p, y):
    
    p = max(min(p, 1. - 10e-15), 10e-15)
    return -log(p) if y == 1. else -log(1. - p)


def data(path, D):

    for t, row in enumerate(DictReader(open(path))):
        # process id
        ID = row['id']
        del row['id']

        # process clicks
        y = 0.
        if 'click' in row:
            if row['click'] == '1':
                y = 1.
            del row['click']
            
        x = []
        for key in row:
            value = row[key]
            
            index = hash(key+'_'+value) % D
            x.append(index)

        yield t, ID, x, y #date, 


##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()
# initialize ourselves a learner
learner = ftrl_proximal(alpha_site, beta_site, L1_site, L2_site, D, interaction_site)

for e in xrange(epoch):
    loss = 0.
    count = 0

    for t, ID, x, y in data(train_site_0, D): 
        
        p = learner.predict(x)

        if (holdout and t % holdout == 0): 
        
            loss += logloss(p, y)
            count += 1
        else:
            # step 2-2, update learner with label (click) information
            learner.update(x, p, y)
        
        if t % 2500000 == 0 and t > 1:
            print(' %s\tencountered: %d\tcurrent logloss: %f' % (
                datetime.now(), t, loss/count))
                
    print('Epoch %d finished, validation logloss: %f, elapsed time: %s' % (
        e, loss/count, str(datetime.now() - start)))

##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()

learner2 = ftrl_proximal(alpha_app, beta_app, L1_app, L2_app, D, interaction_app)
# start training
for e in xrange(epoch):
    loss = 0.
    count = 0

    for t, ID, x, y in data(train_site_2, D):  #
    
        p = learner2.predict(x)

        if (holdout and t % holdout == 0): 
        
            loss += logloss(p, y)
            count += 1
        else:
            
            learner2.update(x, p, y)
        
        if t % 2500000 == 0 and t > 1:
            print(' %s\tencountered: %d\tcurrent logloss: %f' % (
                datetime.now(), t, loss/count))
                
    print('Epoch %d finished, validation logloss: %f, elapsed time: %s' % (
        e, loss/count, str(datetime.now() - start)))

##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()
# initialize ourselves a learner
learner = ftrl_proximal(alpha_site, beta_site, L1_site, L2_site, D, interaction_site)

for e in xrange(epoch):
    loss = 0.
    count = 0

    for t, ID, x, y in data(train_app_0, D): 
        
        p = learner.predict(x)

        if (holdout and t % holdout == 0): 
        
            loss += logloss(p, y)
            count += 1
        else:
            # step 2-2, update learner with label (click) information
            learner.update(x, p, y)
        
        if t % 2500000 == 0 and t > 1:
            print(' %s\tencountered: %d\tcurrent logloss: %f' % (
                datetime.now(), t, loss/count))
                
    print('Epoch %d finished, validation logloss: %f, elapsed time: %s' % (
        e, loss/count, str(datetime.now() - start)))

##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()

learner2 = ftrl_proximal(alpha_app, beta_app, L1_app, L2_app, D, interaction_app)
# start training
for e in xrange(epoch):
    loss = 0.
    count = 0

    for t, ID, x, y in data(train_app_2, D):  #
    
        p = learner2.predict(x)

        if (holdout and t % holdout == 0): 
        
            loss += logloss(p, y)
            count += 1
        else:
            
            learner2.update(x, p, y)
        
        if t % 2500000 == 0 and t > 1:
            print(' %s\tencountered: %d\tcurrent logloss: %f' % (
                datetime.now(), t, loss/count))
                
    print('Epoch %d finished, validation logloss: %f, elapsed time: %s' % (
        e, loss/count, str(datetime.now() - start)))

##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()
# initialize ourselves a learner
learner = ftrl_proximal(alpha_site, beta_site, L1_site, L2_site, D, interaction_site)

for e in xrange(epoch):
    loss = 0.
    count = 0

    for t, ID, x, y in data(train_app_3, D): 
        
        p = learner.predict(x)

        if (holdout and t % holdout == 0): 
        
            loss += logloss(p, y)
            count += 1
        else:
            # step 2-2, update learner with label (click) information
            learner.update(x, p, y)
        
        if t % 2500000 == 0 and t > 1:
            print(' %s\tencountered: %d\tcurrent logloss: %f' % (
                datetime.now(), t, loss/count))
                
    print('Epoch %d finished, validation logloss: %f, elapsed time: %s' % (
        e, loss/count, str(datetime.now() - start)))

##############################################################################
# start training #############################################################
##############################################################################

start = datetime.now()

learner2 = ftrl_proximal(alpha_app, beta_app, L1_app, L2_app, D, interaction_app)
# start training
for e in xrange(epoch):
    loss = 0.
    count = 0

    for t, ID, x, y in data(train_app_5, D):  #
    
        p = learner2.predict(x)

        if (holdout and t % holdout == 0): 
        
            loss += logloss(p, y)
            count += 1
        else:
            
            learner2.update(x, p, y)
        
        if t % 2500000 == 0 and t > 1:
            print(' %s\tencountered: %d\tcurrent logloss: %f' % (
                datetime.now(), t, loss/count))
                
    print('Epoch %d finished, validation logloss: %f, elapsed time: %s' % (
        e, loss/count, str(datetime.now() - start)))

##############################################################################
# start testing, and build Kaggle's submission file ##########################
##############################################################################

with open(submission, 'w') as outfile:
    outfile.write('id,click\n')
    for t, ID, x, y in data(train_site_0, D): #date, 
        p = learner.predict(x)
        outfile.write('%s,%s\n' % (ID, str(p)))
    for t, ID, x, y in data(train_site_2, D): #date, 
        p = learner2.predict(x)
        outfile.write('%s,%s\n' % (ID, str(p)))
    for t, ID, x, y in data(train_app_0, D): #date, 
        p = learner.predict(x)
        outfile.write('%s,%s\n' % (ID, str(p)))
    for t, ID, x, y in data(train_app_2, D): #date, 
        p = learner2.predict(x)
        outfile.write('%s,%s\n' % (ID, str(p)))
    for t, ID, x, y in data(train_app_3, D): #date, 
        p = learner.predict(x)
        outfile.write('%s,%s\n' % (ID, str(p)))
    for t, ID, x, y in data(train_app_5, D): #date, 
        p = learner2.predict(x)
        outfile.write('%s,%s\n' % (ID, str(p)))
