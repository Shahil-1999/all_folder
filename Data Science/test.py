import pandas as pd
# import numpy as np 
from sklearn.model_selection import train_test_split
# from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv("breast-cancer.csv")
df = df.iloc[:,1:6]   # Feature Selection
# a = df.corr() find correlation
# print(df.isnull().sum())    #checking any null value present or not
# df = SelectKBest(score_func=chi2,k =3)
# pipe = make_pipeline(df)
# print(df)
# print(df.max())

x_train,x_test,y_train,y_test = train_test_split(df.drop(columns=['diagnosis']),df['diagnosis'],test_size=0.2,random_state=42)
# print(y_test,x_train)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le = le.fit(y_train)
# print(le.classes_)
y_train = le.transform(y_train)
y_test = le.transform(y_test)
# print(y_test)
# Traning the classifier
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)
# preds = clf.predict(y_test)
# print(preds)
# print(list(df.keys()))



a = float(input("radius_mean (6.981 - 28.11): "))
b = float(input("texture_mean (9.71 - 39.28): "))
c = float(input("perimeter_mean: (43.79 - 188.5) "))
d = float(input("area_mean(143.5 - 2501): "))

preds = clf.predict([[a, b, c, d]])
print(preds)
