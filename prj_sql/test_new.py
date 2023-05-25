import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("C:/Users/kshah/OneDrive/Desktop/prj_sql/breast-cancer.csv")
# Feature Selection
# a2 = df.corr()   
# x2 = a2['diagnosis'].sort_values(ascending=False)
df = df[['smoothness_se','fractal_dimension_mean','texture_se','symmetry_se']].copy()
print(df.describe())

# x_train, x_test, y_train, y_test = train_test_split(
#     df.drop(columns=['diagnosis']), df['diagnosis'], test_size=0.2, random_state=42)

# clf = DecisionTreeClassifier()
# clf.fit(x_train, y_train)




# preds = clf.predict(
# [[radius_mean, texture_mean, perimeter_mean, area_mean]])
# f_pred = (' '.join(preds))