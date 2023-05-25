from flask import Flask, request, render_template
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
app = Flask(__name__)
@app.route('/')


def index ():
    return render_template('btn.htm')

@app.route("/breastCancer")
def breastCancer():
    return render_template('breastcancer.htm')

@app.route('/breast', methods = ['POST'])
def breast():

    df = pd.read_csv('C:/Users/kshah/OneDrive/Desktop/all folders/Machine Learning/br.csv')

    df = df.iloc[:, 1:6]


    from sklearn import svm

    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['diagnosis']), df['diagnosis'], test_size=0.2, random_state=42)
    clf = svm.SVC(kernel='linear')
    clf.fit(x_train, y_train)





    # radius_mean = input("Please enter radius_mean Range(6.981 - 28.11): ")
    radius_mean = request.form['radius_mean']


    # texture_mean = input("Please enter texture_mean (9.71 - 39.28): ")
    texture_mean = request.form['texture_mean']



    # perimeter_mean= input("Please enter perimeter_mean (43.79 - 188.5): ")
    perimeter_mean = request.form['perimeter_mean']



    # area_mean = input("Please enter area_mean(143.5 - 2501): ")
    area_mean = request.form['area_mean']



    preds = clf.predict([[radius_mean, texture_mean, perimeter_mean, area_mean]])
    f_pred = (' '.join(preds))

    if f_pred == 'B':
        b = 'Benign'
        
    else:
        b = 'Malignant'
       
        
    return render_template('br_pass.html', preds = b)




@app.route("/parkinson")
def parkinson():
    
    return render_template('a.html')

@app.route('/park', methods = ['POST'])
def getvalue():
     



    df = pd.read_csv('C:/Users/kshah/OneDrive/Desktop/all folders/Machine Learning/parkinsons.csv')

    # print(df.info())
    # print(df.describe())
    df.isnull().sum()#checking for missing values



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

        # Splitting the data into testing and training set
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['status']), df['status'], test_size=0.2, random_state=42)



    # Model Training (DecisionTreeClassifier)
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)

    

    # D2 = input("Enter your First nonlinear dynamical complexity measures (142 - 367)")
    D2 = request.form['D2']
    # RPDE = input('Enter your second nonlinear dynamical complexity measures (25 - 68)')
    RPDE = request.form['RPDE']
    # PPE = input('Enter your third nonlinear measures of fundamental frequency variation (4 - 52)')
    PPE = request.form['PPE']
    # spread2 = input('Enter your nonlinear fundamental frequency variation (0 - 45)')
    spread2 = request.form['spread2']
    # DFA = input('Enter your Signal fractal scaling exponent (57 - 82)')
    DFA = request.form['DFA']
    # HNR = input('Enter your ratio of noise to tonal components in the voice (844 - 3304)')
    HNR = request.form['HNR']
    # Shimmer_APQ3 = input('Enter your Several measures of variation in amplitude(0 - 5)')
    Shimmer_APQ3 = request.form['Shimmer_APQ3']
    # MDVP_Jitter= input('Enter your Several measures of variation in fundamental frequency (0 - 3)')
    MDVP_Jitter = request.form['MDVP_Jitter']
    


    preds = clf.predict([[D2, RPDE, PPE, spread2, DFA, HNR, Shimmer_APQ3, MDVP_Jitter]])
    print(preds)
    print(D2, RPDE, PPE, spread2, DFA, HNR, Shimmer_APQ3, MDVP_Jitter)
    p = ""

    if preds == 0:
        p = 'Not Affected'
        
        
    else:
        preds == 1
        p = ' Affected'
        
    return render_template('b.html', preds = p)





    
app.run(debug=True)