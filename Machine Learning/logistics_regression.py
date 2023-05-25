# Train a logistic regression classifier to predict whether a flower is iris virginica or not
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt


iris = datasets.load_iris()
# print(list(iris.keys())) # To show how many keys present in iris
# print(iris['data'].shape) # shape of data
# print(iris['target'])
# print(iris['DESCR'])  # Data Descreption 

X = iris["data"][:, 3 :] # Take only 3rd coulmn data(3rd features)(here 4 column sapel leangth, sapel width, patel length, patel weigth)
y = (iris["target"] == 2).astype(np.int)    # Upto this if we print(y) then, if y value = 2 satisfy then it print true or false. (0 = setosa, 1=versicolor, 2= virginica).(if we dont want "true or false" then we use[.astype(np.int)] it convert True or False into 0 or 1

# Train a logistic regression classifier
clf = LogisticRegression()
clf.fit(X,y)

# Predect only one features (In iris there are 4 features)
example = clf.predict(([[2.6]]))
print(example)

# Using matplotlib to plot the visualization
X_new = np.linspace(0,3,1000).reshape(-1,1) #(0,3,1000) means it provide us 0 to 3 equally linearly spaced 1000 elements, (-1,1) means it provide -1x1 array(1D array)
y_prob = clf.predict_proba(X_new)
#print(y_prob)  # It predict probablity, predict actual probablity value
plt.plot(X_new, y_prob[:,1])    # only gives us 1 row
plt.show()
