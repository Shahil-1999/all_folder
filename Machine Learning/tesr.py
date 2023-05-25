import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold
diabetes = pd.read_csv('diabetes.csv')

# print(df.info())
# print(df.describe())
a = diabetes.corr()   #Feature Selection
x = a['Outcome'].sort_values(ascending=False)
diabetes = diabetes.iloc[:,1:]  
a = diabetes.isnull().sum()  # Check any null value present or not
print(diabetes.head())
print(x)
# print(diabetes.shape)





body_p = pd.read_csv('bodyPerformance.csv')

# Converting Object to int
class1 = {'A':0, 'B':1,'C':2,'D':3}
body_p['class'] = body_p['class'].map(class1)

#Feature Selection based on their correlation
a1 = body_p.corr()   
x1 = a1['class'].sort_values(ascending=False)
dfnew = body_p[['body fat_%','weight_kg','diastolic','age','height_cm','systolic','class']].copy() 
# print(dfnew['class'].value_counts())

# print(dfnew.head())




