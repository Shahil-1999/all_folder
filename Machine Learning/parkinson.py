

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 



df = pd.read_csv('C:/Users/kshah/OneDrive/Desktop/all folders/Machine Learning/parkinsons.csv')

# print(df.info())
# print(df.describe())
df.isnull().sum()#checking for missing values


#dropping column axis = 1; dropping row then axis = 0
#Data Pre-Processing - Seperating Features and Target variables according to their Correlation

df.drop(["name",'spread1', 'MDVP:Flo(Hz)','MDVP:Fhi(Hz)','MDVP:Fo(Hz)'], axis=1, inplace=True)
columns = list(df.columns)
for column in columns:
    if column == "status":
        continue

    filtered_columns = [column]
    for col in df.columns:
        if (column == col) | (column == "status"):
            continue
        cor_val = df[column].corr(df[col])
        if cor_val > 0.75:
            columns.remove(col)
            continue
        else:
            filtered_columns.append(col)
    df = df[filtered_columns]
    # print(df)
    
    
# df.isnull().sum() #checking null value


# converting Data in the form of hundred
# df.iloc[:,:8] = (df.iloc[:, :8])

# print(df.describe())





# #Plotting Heatmap
# # plt.figure(figsize=(25, 7))
# # p = sns.heatmap(df.corr(), annot=True)
# # plt.show()


# # plotting bar figure on STATUS column
# # sns.set_style('whitegrid')
# # sns.set_context('paper')
# # sns.set_palette('GnBu_d')
# # a = sns.catplot(x='status', data=df, kind='count')
# # plt.title('Number of Samples in Each Class')
# # a.set(ylabel='Number of Samples', xlabel='Have Parkinson')

# # plt.show()

# #histogram
# # df.hist(figsize=(25,7))
# # plt.show()
# #We can see some of the data is normally distributed and most of the attributes are right skewed



# Splitting the data into testing and training set
x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['status']), df['status'], test_size=0.2, random_state=42)


# print(x_train.to_string())
# print(y_train.to_string())


# # Data Standardization
# scaler = StandardScaler()
# clf = scaler.fit(x_train)


# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)




# Model Training (DecisionTreeClassifier)
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)



# # # Model Evaluation
# # # Accuracy Score

# # # Accuracy Score on training data
# # x_train_pred = clf.predict(x_train)
# # training_data_accuracy = accuracy_score(y_train, x_train_pred)
    
# # print('Accuracy (Training Data) :', training_data_accuracy*100,'%')


# # # Accuracy Score on test data
# # x_test_pred = clf.predict(x_test)
# # testing_data_accuracy = accuracy_score(y_test, x_test_pred)
    

# # print('Accuracy (Testing Data) :', testing_data_accuracy*100,'%')
    

D2 = input("Enter your First nonlinear dynamical complexity measures (142 - 367)")
RPDE = input('Enter your second nonlinear dynamical complexity measures (25 - 68)')
PPE = input('Enter your third nonlinear measures of fundamental frequency variation (4 - 52)')
spread2 = input('Enter your nonlinear fundamental frequency variation (0 - 45)')
DFA = input('Enter your Signal fractal scaling exponent (57 - 82)')
HNR = input('Enter your ratio of noise to tonal components in the voice (844 - 3304)')
Shimmer_APQ3 = input('Enter your Several measures of variation in amplitude(0 - 5)')
MDVP_Jitter= input('Enter your Several measures of variation in fundamental frequency (0 - 3)')


preds = clf.predict([[D2, RPDE, PPE, spread2, DFA, HNR, Shimmer_APQ3, MDVP_Jitter]])
print(preds)


# p = ""

# if preds == 0:
#     p = 'Not Affected'
    
    
# else:
#     preds == 1
#     p = ' Affected'

# print(p)
# # if preds == 0:
# #     print('The patient does not have Parkinson')
# # elif preds == 1:
# #     print('The patient has Parkinson')
# # else:
# #     print('Some error in processing')

