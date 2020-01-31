# -*- coding: utf-8 -*-
"""Multiple_Linear_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZlmejTxt0nk9mBO8h6k7dYCujOET81cf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

data = pd.read_csv("sample_data/Advertising.csv")

data.head()
data.drop(['Unnamed: 0'], axis =1)

Xs = data.drop(['sales', 'Unnamed: 0'], axis = 1)
y = data['sales'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(Xs,y)

print(reg.coef_)
print(reg.intercept_)

reg.score(Xs, y)

X = np.column_stack((data['TV'], data['radio'], data['newspaper']))
y = data['sales']

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())