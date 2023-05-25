import os

while (True):
    print("Welcome To CodersHospital")
    
    #creating database connectivity
    import mysql.connector
    passwd = ("Shahil")

    mysql = mysql.connector.connect(host = "localhost", user = "root", passwd = "Shahil@1999")
    mycursor = mysql.cursor()
    mycursor.execute("create database if not exists city_hospitals")
    mycursor.execute("use city_hospitals")


    # creating the tables for storing patient details.
    mycursor.execute("create table if not exists patient_detail(patient_id varchar(4) primary key, name varchar(30) ,sex varchar(15),age int(3),address varchar(50),contact varchar(15),mail varchar(40), disease varchar(80), breasr_cancer_prediction varchar(70), parkinson_disease_prediction varchar(70))")

  
    # creating table for storing the username and password of the user
    mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")


  
    while (True):
        print("""       
                        1. Registration
                        2. Sign In
                        3. Show Admin database
                        """)

        r = int(input("enter your choice: "))
        if r == 1:
            print("""
                !!!!!!!!!!Register Yourself!!!!!!!!""")
            u = input("Input your username!!:")
            p = input("Input the password (Password must be strong!!!): ")

            mycursor.execute("insert into user_data values('" + u + "','" + p + "')")
            mysql.commit()

            print("""
                ============================================
                !!Well Done!!Registration Done Successfully!!
                ============================================
                                                    """)
            os.system("pause")

            
        # IF USER WANTS TO LOGIN
        elif r == 2:
            print("""
                    ==================================
                    !!!!!!!!  {{Sign In}}  !!!!!!!!!!
                    ==================================
                                                        """)
            un = input("Enter Username!!: ")
            ps = input("Enter Password!!: ")
            
            
            mycursor.execute("select password from user_data where username='" + un + "'")
            row = mycursor.fetchall()
            for i in row:
                a = list(i)
                if a[0] == str(ps):
                    while(True):
                        print("""
                                    1.Administration
                                    2.Patient(Details)
                                    3.Show patient database
                                    4. Sign Out
                                                    """)

                        a = int(input("ENTER YOUR CHOICE: "))
                        if a == 1:
                            print("""
                                    1. Log patient Record
                                    2. Discharge Summary
                                    """)
                           

                
                            x = int(input("ENTER YOUR CHOICE: "))
                            if x == 1:

                                print("""
                                        1. Add New Patient
                                        
                                        """)

                                b = int(input("Enter your Choice: "))
                                
                                
                                # adding new patient
                                if b == 1:
                                    patient_id = input("Enter patient_id: ")
                                    name = input("Enter your name: ")
                                    sex = input("Enter the gender: ")
                                    age = input("Enter age: ")
                                    address = input("Enter address: ")
                                    contact = input("Contact Details: ")
                                    mail = input("Enter Mail: ")
                                    desease = input("Enter Desease: ")
                                    bill = input("Have you breast cancer? (y/n):")
                                    p_pred = input("Have parkinson: ")
                                    f_pred = "NA"
                                    p_pred = "NA"

                                    if bill == "y":
                                        import pandas as pd
                                        import numpy as np
                                        from sklearn.model_selection import train_test_split
                                        from sklearn.pipeline import Pipeline,make_pipeline
                                        from sklearn.tree import DecisionTreeClassifier


                                        df = pd.read_csv("breast-cancer.csv")
                                        df = df.iloc[:,1:6]   # Feature Selection
                                        x_train,x_test,y_train,y_test = train_test_split(df.drop(columns=['diagnosis']),df['diagnosis'],test_size=0.2,random_state=42)
                                        
                                        clf = DecisionTreeClassifier()
                                        clf.fit(x_train, y_train)



                                        a = float(input("radius_mean (6.981 - 28.11): "))
                                        b = float(input("texture_mean (9.71 - 39.28): "))
                                        c = float(input("perimeter_mean: (43.79 - 188.5) "))
                                        d = float(input("area_mean(143.5 - 2501): "))
                                        

                                        preds = clf.predict([[a, b, c, d]])
                                        f_pred =(' '.join(preds))
                                        
                                    if p_pred == "y":
                                        
                                        import os
                                        import pandas as pd
                                        import numpy as np
                                        import seaborn as sns
                                        import matplotlib.pyplot as plt
                                        import voice.speak as sp
                                        import voice.command as cmd
                                        from sklearn.model_selection import train_test_split
                                        from sklearn.preprocessing import StandardScaler
                                        from sklearn import svm
                                        from sklearn.metrics import accuracy_score
                                        from sklearn.tree import DecisionTreeClassifier
                                        import warnings
                                        warnings.filterwarnings("ignore", category=DeprecationWarning)
                                        df = pd.read_csv('C:/Users/kshah/OneDrive/Desktop/Machine Learning/parkinsons.csv')

 
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
                                            
                                            
                                        df.isnull().sum() #checking null value


                                        # converting Data in the form of hundred
                                        df.iloc[:,:8] = (df.iloc[:, :8]).mul(100).astype(int)
                                        # print(df.describe())





                                        #Plotting Heatmap
                                        # plt.figure(figsize=(25, 7))
                                        # p = sns.heatmap(df.corr(), annot=True)
                                        # plt.show()


                                        # plotting bar figure on STATUS column
                                        # sns.set_style('whitegrid')
                                        # sns.set_context('paper')
                                        # sns.set_palette('GnBu_d')
                                        # a = sns.catplot(x='status', data=df, kind='count')
                                        # plt.title('Number of Samples in Each Class')
                                        # a.set(ylabel='Number of Samples', xlabel='Have Parkinson')

                                        # plt.show()

                                        #histogram
                                        # df.hist(figsize=(25,7))
                                        # plt.show()
                                        #We can see some of the data is normally distributed and most of the attributes are right skewed



                                        # Splitting the data into testing and training set
                                        x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['status']), df['status'], test_size=0.2, random_state=42)



                                        # Data Standardization
                                        # scaler = StandardScaler()
                                        # a = scaler.fit(x_train)


                                        # x_train = scaler.transform(x_train)
                                        # x_test = scaler.transform(x_test)




                                        # Model Training (DecisionTreeClassifier)
                                        clf = DecisionTreeClassifier()
                                        clf.fit(x_train, y_train)



                                        # # Model Evaluation
                                        # # Accuracy Score

                                        # # Accuracy Score on training data
                                        # x_train_pred = clf.predict(x_train)
                                        # training_data_accuracy = accuracy_score(y_train, x_train_pred)
                                            
                                        # print('Accuracy (Training Data) :', training_data_accuracy*100,'%')


                                        # # Accuracy Score on test data
                                        # x_test_pred = clf.predict(x_test)
                                        # testing_data_accuracy = accuracy_score(y_test, x_test_pred)
                                            

                                        # print('Accuracy (Testing Data) :', testing_data_accuracy*100,'%')
                                            
                                        sp.speak("Enter your First nonlinear dynamical complexity measures (142 - 367)")
                                        D2 = input("Enter your First nonlinear dynamical complexity measures (142 - 367): ")
                                        
                                        sp.speak("Enter your second nonlinear dynamical complexity measures (25 - 68)")
                                        RPDE = input('Enter your second nonlinear dynamical complexity measures (25 - 68): ')
                                        
                                        sp.speak('Enter your third nonlinear measures of fundamental frequency variation (4 - 52)')
                                        PPE = input('Enter your third nonlinear measures of fundamental frequency variation (4 - 52): ')
                                        
                                        sp.speak("Enter your nonlinear fundamental frequency variation (0 - 45)")
                                        spread2 = input('Enter your nonlinear fundamental frequency variation (0 - 45): ')
                                        
                                        sp.speak("Enter your Signal fractal scaling exponent (57 - 82)")
                                        DFA = input('Enter your Signal fractal scaling exponent (57 - 82): ')
                                        
                                        sp.speak("Enter your ratio of noise to tonal components in the voice (844 - 3304)")
                                        HNR = input('Enter your ratio of noise to tonal components in the voice (844 - 3304): ')
                                        
                                        sp.speak("Enter your Several measures of variation in amplitude(0 - 5)")
                                        Shimmer_APQ3 = input('Enter your Several measures of variation in amplitude(0 - 5): ')
                                        
                                        sp.speak("Enter your Several measures of variation in fundamental frequency (0 - 3)")
                                        MDVP_Jitter= input('Enter your Several measures of variation in fundamental frequency (0 - 3): ')


                                        p_pred = clf.predict([[D2, RPDE, PPE, spread2, DFA, HNR, Shimmer_APQ3, MDVP_Jitter]])

                                        p_pred = (','.join(str(x) for x in p_pred))

                                        if p_pred == 1:
                                            p_pred = 'The patient has Parkinson'
                                            
                                        else:
                                            p_pred == 0
                                            p_pred = 'The patient does not have Parkinson'
                                    



#  print("Enter your First nonlinear dynamical complexity measures (142 - 367)")
#     sp.speak("Enter your First nonlinear dynamical complexity measures (142 - 367)")
#     D2 = cmd.takeCommand().lower()
#     print(D2)
#     sp.speak(D2)
    
#     print("Enter your second nonlinear dynamical complexity measures (25 - 68)")
#     sp.speak("Enter your second nonlinear dynamical complexity measures (25 - 68)")
#     RPDE = cmd.takeCommand().lower()
#     print(RPDE)
#     sp.speak(RPDE)
    
    
#     print('Enter your third nonlinear measures of fundamental frequency variation (4 - 52)')
#     sp.speak('Enter your third nonlinear measures of fundamental frequency variation (4 - 52)')
#     PPE = cmd.takeCommand().lower()
#     print(PPE)
#     sp.speak(PPE)
    
#     print("Enter your nonlinear fundamental frequency variation (0 - 45)")
#     sp.speak("Enter your nonlinear fundamental frequency variation (0 - 45)")
#     spread2 = cmd.takeCommand().lower()
#     print(spread2)
#     sp.speak(spread2)
    
#     print("Enter your Signal fractal scaling exponent (57 - 82)")
#     sp.speak("Enter your Signal fractal scaling exponent (57 - 82)")
#     DFA = cmd.takeCommand().lower()
#     print(DFA)
#     sp.speak(DFA)
    
#     print("Enter your ratio of noise to tonal components in the voice (844 - 3304)")
#     sp.speak("Enter your ratio of noise to tonal components in the voice (844 - 3304)")
#     HNR = cmd.takeCommand().lower()
#     print(HNR)
#     sp.speak(HNR)
    
#     print("Enter your Several measures of variation in amplitude(0 - 5)")
#     sp.speak("Enter your Several measures of variation in amplitude(0 - 5)")
#     Shimmer_APQ3 = cmd.takeCommand().lower()
#     print(Shimmer_APQ3)
#     sp.speak(Shimmer_APQ3)
    
#     print("Enter your Several measures of variation in fundamental frequency (0 - 3)")
#     sp.speak("Enter your Several measures of variation in fundamental frequency (0 - 3)")
#     MDVP_Jitter = cmd.takeCommand().lower()
#     print(MDVP_Jitter)
#     sp.speak(MDVP_Jitter)
                                        
    
                                    mycursor.execute("insert into patient_detail values('" + patient_id + "','" + name + "','" + sex + "','" +age + "','" + address + "','" + contact + "','" + mail + "','" + desease + "','" + f_pred + "','" + p_pred + "')")
                                    mysql.commit()
                                    print("""
                                            ====================================
                                            !!!!!!!Registered Successfully!!!!!!
                                            ====================================
                                                            """)
                                                                    


                                    os.system("pause")

                                else:
                                    print("Choose Valid Option")
                            
                                


                            # dischare process
                            elif x == 2:
                                name = input("Enter the Patient Name: ")
                                mycursor.execute("select * from patient_detail where name='" + name + "'")
                                row = mycursor.fetchall()
                                for i in row:
                                    b1 = 0
                                    v1 = list(i)
                                    k1 = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT", "DISEASE","PREDICTED DISEASE"]
                                    d1 = dict(zip(k1, v1))
                                    print(d1)

                                bill = input("Has he paid all the bills? (y/n):")
                                if bill == "y":
                                    mycursor.execute("delete from patient_detail where name='" + name + "'")
                                    mysql.commit()
                                else:
                                    print("please clear your bill")

                            else:
                                print("Choose Valid Option")
                                os.system("pause")

           
                        # if user wants to see the details of PATIENT
                        elif a == 2:
                
                            name = input("Enter the Patient Name: ")
                            mycursor.execute("select * from patient_detail where name='" + name + "'")
                            row = mycursor.fetchall()
                            for i in row:
                                b = 0
                                v = list(i)
                                k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT", "DISEASE","PREDICTED DISEASE"]
                                d = dict(zip(k, v))
                                print(d)
                        
                        #if user wants to show all patient records
                        elif a == 3:
                            mycursor.execute("select * from patient_detail")
                            row1 = mycursor.fetchall()
                            for i in row1:
                                b = 0
                                v = list(i)
                                k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT", "DISEASE","PREDICTED DISEASE"]
                                d = dict(zip(k, v))
                                print(d)
                               

      
                        #SIGN OUT
                        elif a == 4:
                                break

                        else:
                            print("Choose Valid Option")
                        
        
                # IF THE USERNAME AND PASSWORD IS NOT IN THE DATABASE
                else:
                    break

        elif r == 3:
            
            print("""
                                    1. Staff's Data
                                    
                                                    """)
            i = int(input("Enter Your Choice: "))
            if i == 1:
                pwd = str(input("Enter Password: "))
                if pwd == passwd:
                    while(True):
                        print("""
                                        1. Show Staff's Data
                                        2. Delete staff's data
                                        
                                                        """)
                        x = int(input("Enter your Choice: "))
                        if x == 1:
                            mycursor.execute("select * from user_data")
                            row1 = mycursor.fetchall()
                            for i in row1:
                                b = 0
                                v = list(i)
                                k = ["USERNAME", "PASSWORD"]
                                d = dict(zip(k, v))
                                print(d)
                        elif x == 2:
                            un = input("Enter the Staff Name: ")
                            sure = input("Are You Sure? (y/n):")

                            if sure == "y":
                                mycursor.execute("delete from user_data where username='" + un + "'")
                                mysql.commit()
                                print("Successfully Staff deleted")
                            else:
                                ("Staff Not Found")
                            os.system("pause")
                            

                        else:
                            print("Choose Valid Option")
                else:
                    print("Invalid Password")
                    break
            else:
                print("Choose Valid Option")
        else:
            print("Choose Valid Option")