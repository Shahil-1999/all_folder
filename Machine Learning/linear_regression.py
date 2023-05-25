import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes() #To load database dataset
diabetes_x = diabetes.data[:, np.newaxis, 3] # Here ':' means all, newaxis means that allows us to change or expand the dimension of a numpy array in the position in which it has been entered. 2 means index number.
# print(diabetes_x)
diabetes_x_train = diabetes_x[:-30]  #To train last 20 data
diabetes_x_test = diabetes_x[-30:]  #To test first 20 data ,,,,,,,, these two lines is FEATURES

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]   # These two lines are LABELS


model = linear_model.LinearRegression()
model.fit(diabetes_x_train, diabetes_y_train)   # To fit our data , means we draw a line by the help of our data and that line save into linear model.
diabetes_y_predict = (model.predict(diabetes_x_test))


print("Mean Squared Error is: ", mean_squared_error(diabetes_y_test, diabetes_y_predict))
print("Weight: ", model.coef_)
print("Intercept: ", model.intercept_)

plt.scatter(diabetes_x_test, diabetes_y_test)
plt.plot(diabetes_x_test, diabetes_y_predict)

plt.show()