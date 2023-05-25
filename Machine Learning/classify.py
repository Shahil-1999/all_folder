# Loading Required Modules
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


# Loading dataset

iris = datasets.load_breast_cancer()

# Printing Description and features
print(iris.DESCR)   # printing Description (not mandatory)
# print(iris['target_names'])
# print(list(iris.keys()))
feature = iris.data
labels = iris.target
# print(feature[0], labels[0])    # (not mandatory) this is for example(it gives us output 0,1,2,3,n as per your decreption, here output 0 means "setosa", 1 means "versicolor"...)

# Traning the classifier
clf = LogisticRegression()
clf.fit(feature, labels)

# Predict according to new value
a = float(input("sepal length: "))
b = float(input("sepal width: "))
c = float(input("petal length: "))
e = float(input("petal width: "))
f = float(input("petal width: "))
g = float(input("petal width: "))
h = float(input("petal width: "))
i = float(input("petal width: "))
j = float(input("petal width: "))
k = float(input("petal width: "))
l = float(input("petal width: "))
m = float(input("petal width: "))
n = float(input("petal width: "))
o = float(input("petal width: "))
p = float(input("petal width: "))
q = float(input("petal width: "))
r = float(input("petal width: "))
s = float(input("petal width: "))
t = float(input("petal width: "))
u = float(input("petal width: "))
v = float(input("petal width: "))
w = float(input("petal width: "))
x = float(input("petal width: "))
y = float(input("petal width: "))
z = float(input("petal width: "))
za = float(input("petal width: "))
zb = float(input("petal width: "))
zc = float(input("petal width: "))
zd = float(input("petal width: "))
ze = float(input("petal width: "))

preds = clf.predict([[a, b, c, e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,za,zb,zc,zd,ze]])
a = (iris['target_names'][preds])
for i in(a): 
    print(i)
