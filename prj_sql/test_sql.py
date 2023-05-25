import os
import voice.speak as sp
import voice.command as cmd
import voice.wish as ws

while (True):
    

    # creating database connectivity
    import mysql.connector
    passwd = ("Shahil")

    mysql = mysql.connector.connect(host="localhost", user="root", passwd="Shahil@1999")
    mycursor = mysql.cursor()
    mycursor.execute("create database if not exists city_hospitals")
    mycursor.execute("use city_hospitals")

    # creating the tables for storing patient details.
    mycursor.execute("create table if not exists patient_detail(name varchar(30) primary key,sex varchar(15),age int(3),address varchar(50),contact varchar(15),mail varchar(30),disease varchar(20), predicted_disease varchar(20))")

    # creating table for storing the username and password of the user
    mycursor.execute(
        "create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")

    while (True):
        ws.wishMe()
        print("Welcome To CodersHospital")
        sp.speak("Welcome To CodersHospital")
        
        print("""       
                        1. Registration
                        2. Sign In
                        3. Show Admin database
                        """)
        sp.speak("""press 1 for Registration
                    press 2 for Sign In
                    press 3 for Show Admin database""")
        
        
        r = int(input("enter your choice: "))
        if r == 1:
            print("""
                !!!!!!!!!!Register Yourself!!!!!!!!""")
            u = input("Input your username!!:")
            p = input("Input the password (Password must be strong!!!): ")

            mycursor.execute(
                "insert into user_data values('" + u + "','" + p + "')")
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
            sp.speak("Please Verify Your Credentials")
            print("Please Enter Your Username")
            sp.speak("Please Enter Your Username")
            un = input("Username!!: ")
            
            print("Please Enter Your Password")
            sp.speak("Please Enter Your Password")
            ps = input("Password!!: ")
            
            

            mycursor.execute(
                "select password from user_data where username='" + un + "'")
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

                                    name = input("Enter your name: ")
                                    sex = input("Enter the gender: ")
                                    age = input("Enter age: ")
                                    address = input("Enter address: ")
                                    contact = input("Contact Details: ")
                                    mail = input("Enter Your Mail Id: ")
                                    desease = input("Enter Desease: ")
                                    bill = input(
                                        "Have breast cancer? (y/n):")
                                    f_pred = "NA"

                                    if bill == "y":

                                        import pandas as pd
                                        import numpy as np
                                        from sklearn.model_selection import train_test_split
                                        from sklearn.pipeline import Pipeline, make_pipeline
                                        from sklearn.tree import DecisionTreeClassifier

                                        df = pd.read_csv("breast-cancer.csv")
                                        # Feature Selection
                                        df = df.iloc[:, 1:6]
                                        x_train, x_test, y_train, y_test = train_test_split(
                                            df.drop(columns=['diagnosis']), df['diagnosis'], test_size=0.2, random_state=42)

                                        clf = DecisionTreeClassifier()
                                        clf.fit(x_train, y_train)


                                    

                                        
                                        sp.speak(
                                            "Please enter radius_mean Range(6.981 - 28.11): ")
                                        print(
                                            "Please enter radius_mean Range(6.981 - 28.11): ")
                                        radius_mean = cmd.takeCommand().lower()

                                        # speak("According to Wikipedia")
                                        print(radius_mean)
                                        sp.speak(radius_mean)

                                        sp.speak(
                                            "Please enter texture_mean (9.71 - 39.28): ")
                                        print(
                                            "Please enter texture_mean (9.71 - 39.28): ")

                                        texture_mean = cmd.takeCommand().lower()

                                        # speak("According to Wikipedia")
                                        print(texture_mean)
                                        sp.speak(texture_mean)

                                        sp.speak(
                                            "Please enter perimeter_mean (43.79 - 188.5): ")
                                        print(
                                            "Please enter perimeter_mean (43.79 - 188.5): ")
                                        perimeter_mean = cmd.takeCommand().lower()

                                        # speak("According to Wikipedia")
                                        print(perimeter_mean)
                                        sp.speak(perimeter_mean)

                                        sp.speak(
                                            "Please enter area_mean(143.5 - 2501): ")
                                        print(
                                            "Please enter area_mean(143.5 - 2501): ")
                                        area_mean = cmd.takeCommand().lower()

                                        # speak("According to Wikipedia")
                                        print(area_mean)
                                        sp.speak(area_mean)

                                        preds = clf.predict(
                                            [[radius_mean, texture_mean, perimeter_mean, area_mean]])
                                        f_pred = (' '.join(preds))
                                        sp.speak(f_pred)

                                    mycursor.execute("insert into patient_detail values('" + name + "','" + sex + "','" + age +
                                                     "','" + address + "','" + contact + "','" + mail + "','" + desease + "','" + f_pred + "')")
                                    mysql.commit()
                                    print("""
                                            ====================================
                                            !!!!!!!Registered Successfully!!!!!!
                                            ====================================
                                                            """)

                                    os.system("pause")

                                    from email.message import EmailMessage
                                    import ssl
                                    import os
                                    import smtplib
                                    # from email.mime.multipart import MIMEMultipart
                                    # from email.mime.text import MIMEText

                                    email_sender = "shahil.official.college@gmail.com"
                                    pwd_sender = "utffkbmcqyvfpwip"
                                    receiver = mail
                                    # msg = MIMEMultipart()

                                    subject = f"{name} Health Report"
                                    # message=f"NAME{name}"
                                    body = f"NAME: {name}\n AGE: {age}\n SEX: {sex}\n ADDRESS: {address}\n CONTACT: {contact}\n MAIL: {mail}\n DISEASE: {desease}\n PRIDECTED DISEASE: {f_pred}"
                                    em = EmailMessage()
                                    em['From'] = email_sender

                                    em['To'] = receiver
                                    em['Subject'] = subject
                                    # msg.attach(MIMEText(message))
                                    em.set_content(body)
                                    context = ssl.create_default_context()

                                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                                        smtp.login(email_sender, pwd_sender)
                                        smtp.sendmail(
                                            email_sender, receiver, em.as_string())

                                else:
                                    print("Choose Valid Option")

                            # dischare process
                            elif x == 2:
                                name = input("Enter the Patient Name: ")
                                mycursor.execute(
                                    "select * from patient_detail where name='" + name + "'")
                                row = mycursor.fetchall()
                                for i in row:
                                    b1 = 0
                                    v1 = list(i)
                                    k1 = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT",
                                          "MAIL", "DISEASE", "PREDICTED DISEASE"]
                                    d1 = dict(zip(k1, v1))
                                    print(d1)

                                bill = input(
                                    "Has he paid all the bills? (y/n):")
                                if bill == "y":
                                    mycursor.execute(
                                        "delete from patient_detail where name='" + name + "'")
                                    mysql.commit()
                                else:
                                    print("please clear your bill")

                            else:
                                print("Choose Valid Option")
                                os.system("pause")

                        # if user wants to see the details of PATIENT
                        elif a == 2:

                            name = input("Enter the Patient Name: ")
                            mycursor.execute(
                                "select * from patient_detail where name='" + name + "'")
                            row = mycursor.fetchall()
                            for i in row:
                                b = 0
                                v = list(i)
                                k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT",
                                     "MAIL", "DISEASE", "PREDICTED DISEASE"]
                                d = dict(zip(k, v))
                                print(d)

                        # if user wants to show all patient records
                        elif a == 3:
                            mycursor.execute("select * from patient_detail")
                            row1 = mycursor.fetchall()
                            for i in row1:
                                b = 0
                                v = list(i)
                                k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT",
                                     "MAIL", "DISEASE", "PREDICTED DISEASE"]
                                d = dict(zip(k, v))
                                print(d)

                        # SIGN OUT
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
                                mycursor.execute(
                                    "delete from user_data where username='" + un + "'")
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
