# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 18:41:51 2015

@author: Ivan
"""

import pandas as pd

submit_1 = 'submit_0_2_3_5_part_1.csv'
submit_2 = 'submit_0_2_3_5_part_2.csv'
pred_1 = pd.read_csv(submit_1,index_col = False, header = None, delim_whitespace=True)
pred_2 = pd.read_csv(submit_2,index_col = False, header = None, delim_whitespace=True)

submission = pred_1.append(pred_2,ignore_index=True)
submission.to_csv('ftrl_0_2_3_5.csv',index=False)
