import os

while (True):
    print("Welcome To CodersHospital")
    
    #creating database connectivity
    import mysql.connector
    passwd = ("Shahil")

    mysql = mysql.connector.connect(host = "localhost", user = "root", passwd = "Shahil@1999")
    mycursor = mysql.cursor()
    mycursor.execute("create database if not exists city_ospitals")
    mycursor.execute("use city_hospitals")


    # creating the tables for storing patient details.
    mycursor.execute("create table if not exists patient_detail(name varchar(30) primary key,sex varchar(15),age int(3),address varchar(50),contact varchar(15),desease varchar(20), predicted_disease varchar(20))")

  
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

                                    name = input("Enter your name: ")
                                    sex = input("Enter the gender: ")
                                    age = input("Enter age: ")
                                    address = input("Enter address: ")
                                    contact = input("Contact Details: ")
                                    desease = input("Enter Desease: ")
                                    bill = input("Have you breast cancer? (y/n):")
                                    f_pred = "NA"

                                    if bill == "y":
                                        
                                        import pandas as pd
                                        import numpy as np
                                        from sklearn.model_selection import train_test_split
                                        from sklearn.pipeline import Pipeline,make_pipeline
                                        from sklearn.tree import DecisionTreeClassifier


                                        df = pd.read_csv("breast-cancer.csv")
                                        df = df.iloc[:,1:6]   # Feature Selection
                                        x_train,x_test,y_train,y_test = train_test_split(df.drop(columns=['diagnosis']),df['diagnosis'],test_size=0.2,random_state = 42)
                                        
                                        clf = DecisionTreeClassifier()
                                        clf.fit(x_train, y_train)










                                        import pyttsx3 #pip install pyttsx3
                                        import speech_recognition as sr #pip install speechRecognition
                                        import datetime
                                        import wikipedia #pip install wikipedia
                                        import webbrowser
                                        import os
                                        import smtplib



                                        engine = pyttsx3.init('sapi5')
                                        voices = engine.getProperty('voices') 
                                        # print(voices[1].id)
                                        engine.setProperty('voice', voices[1].id)


                                        # wishMe()
                                            # while True:
                                            #     if 1:
                                                
                                       


                                        def speak(audio):
                                            engine.say(audio)
                                            engine.runAndWait()


                                        # def wishMe():
                                        #     hour = int(datetime.datetime.now().hour)
                                        #     if hour>=0 and hour<12:
                                        #         speak("Good Morning!")

                                        #     elif hour>=12 and hour<18:
                                        #         speak("Good Afternoon")   

                                        #     else:
                                        #         speak("Good Evening")  

                                        #     speak("I am charlie. Please tell me how may I help you")
                                           

                                            
                                                    
                                                    



                                        def takeCommand():
                                            #It takes microphone input from the user and returns string output

                                            r = sr.Recognizer()
                                            with sr.Microphone() as source:
                                                print("Listening...")
                                                r.pause_threshold = 1
                                                audio = r.listen(source)

                                            try:
                                                print("Recognizing...")    
                                                query = r.recognize_google(audio, language = 'en - in')
                                                print(f"User said: {query}\n")

                                            except Exception as e:
                                                # print(e)    
                                                print("Say that again please...")  
                                                return "None"
                                            return query



                                        speak("Please enter radius_mean Range(6.981 - 28.11): ")
                                        print("Please enter radius_mean Range(6.981 - 28.11): ")
                                        radius_mean = takeCommand().lower()
                                                    
                                                            # speak("According to Wikipedia") 
                                        print(radius_mean)
                                        speak(radius_mean)



                                        speak("Please enter texture_mean (9.71 - 39.28): ")
                                        print("Please enter texture_mean (9.71 - 39.28): ")
                                        
                                        texture_mean = takeCommand().lower()
                                                    
                                                            # speak("According to Wikipedia") 
                                        print(texture_mean)
                                        speak(texture_mean)



                                        speak("Please enter perimeter_mean (43.79 - 188.5): ")
                                        print("Please enter perimeter_mean (43.79 - 188.5): ")
                                        perimeter_mean = takeCommand().lower()
                                                    
                                                            # speak("According to Wikipedia") 
                                        print(perimeter_mean)
                                        speak(perimeter_mean)



                                        speak("Please enter area_mean(143.5 - 2501): ")
                                        print("Please enter area_mean(143.5 - 2501): ")
                                        area_mean = takeCommand().lower()
                                                    
                                                            # speak("According to Wikipedia") 
                                        print(area_mean)
                                        speak(area_mean)


                                        # if __name__ == "__main__":
                                            # wishMe()
                                            # # while True:
                                            # #     if 1:
                                                
                                            # speak("radius_mean (6.981 - 28.11): ")
                                            # query = takeCommand().lower()
                                                    
                                            #                 # speak("According to Wikipedia") 
                                            # print(query)
                                            # speak(query)


                                        #         if 'radius' in query:
                                                    
                                        #             info = "radius_mean (6.981 - 28.11): "
                                        #             # speak("According to Wikipedia") 
                                        #             print(info)
                                        #             speak(info)

                                        #         elif 'texture' in query:
                                        #             info1 = "texture_mean (9.71 - 39.28): "
                                        #             print(info1)
                                        #             speak(info1)

                                        #         elif 'parameter' in query:
                                        #             info2 = "perimeter_mean (43.79 - 188.5): "
                                        #             print(info2)
                                        #             speak(info2)


                                        #         elif 'area' in query:
                                        #             info3 = "area_mean(143.5 - 2501): "
                                        #             print(info3)
                                        #             speak(info3)




                                        # a1 = float(input("radius_mean (6.981 - 28.11): "))
                                        # b1 = float(input("texture_mean (9.71 - 39.28): "))
                                        # c1 = float(input("perimeter_mean (43.79 - 188.5): "))
                                        # d1 = float(input("area_mean(143.5 - 2501): "))

                                        preds = clf.predict([[radius_mean,texture_mean,perimeter_mean,area_mean]])
                                        f_pred = (' '.join(preds))
                                        speak(f_pred)
                                        
    
                                    mycursor.execute("insert into patient_detail values('" + name + "','" + sex + "','" +age + "','" + address + "','" + contact + "','" + desease + "','" + f_pred + "')")
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