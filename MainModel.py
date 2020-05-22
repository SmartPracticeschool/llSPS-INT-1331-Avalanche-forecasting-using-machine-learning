# -*- coding: utf-8 -*-
"""pro1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/142zoIPJoKlSYSVogxy1CH_QsSVrXgZxq
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_excel("/content/ava.xlsx")

dataset

sns.heatmap(dataset.isnull())

dataset.isnull().any()

dataset.describe()

dataset.info()

dataset["month"].unique()

dataset["avalanche occurance"].unique()

from sklearn.preprocessing import LabelEncoder
le  = LabelEncoder()
dataset["month"] = le.fit_transform(dataset["month"])
dataset["avalanche occurance"]=le.fit_transform(dataset["avalanche occurance"])

dataset.head()

x = dataset.iloc[:,0:5].values
y = dataset.iloc[:,5:6].values

from sklearn.preprocessing import OneHotEncoder
oh = OneHotEncoder()
z = oh.fit_transform(x[:,0:1]).toarray()
x = np.delete(x,0,axis = 1)
x = np.concatenate((z,x),axis = 1)

x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=0)

from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression()
logistic.fit(x_train,y_train)

import pickle
pickle.dump(logistic,open("Avalanche.pkl","wb"))

y_pred = logistic.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score
logacc = accuracy_score(y_test,y_pred)
logacc

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
cm

from sklearn import metrics
fpr,tpr,threshold, = metrics.roc_curve(y_test,y_pred)
roc_auc = metrics.auc(fpr,tpr)

plt.title("roc")
plt.plot(fpr,tpr,label = 'Auc = %0.2f'%roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([0,1])
plt.ylim([0,1])
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.show()

