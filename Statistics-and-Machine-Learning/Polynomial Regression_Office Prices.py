'''https://www.hackerrank.com/challenges/predicting-office-space-price/problem'''

import math

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

f,n=list(map(int,input().split()))
columns=f+1
rows=n
data=np.zeros((n,f+1))

# creating the dataframe no of houses X F+1
for r in range(0, rows):
    list=input().split()
    for c in range (0,f+1):
        data[r][c]=list[c]


train=pd.DataFrame(data)
# creating the dataframe for test T X F
#Dataset=pd.DataFrame()
t=int(input())
data=np.zeros((t,f))
for r in range(0, t):
    list=input().split()
    for c in range (0,f):
        data[r][c]=list[c]

test=pd.DataFrame(data)
#print('Shape of train data',train.shape)
#print('Shape of test data',test.shape)


X=train.iloc[:,:f] # features
y=train.iloc[:,f:] #price per square foot
#x_train,x_test,y_train,y_test=train_test_split(X,y, random_state=42,test_size=0.2)
poly = PolynomialFeatures(degree = 3)
X=poly.fit_transform(X)
lr=LinearRegression()
lr.fit(X,y)
test=poly.fit_transform(test)
prediction=lr.predict(test)
for i in prediction:
    print(i[0])
