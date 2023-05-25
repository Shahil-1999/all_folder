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
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")   

    else:
        speak("Good Evening")  

    speak("I am charlie. Please tell me how may I help you")       

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

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login(g, p)
#     server.sendmail(g, to, content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()


        if 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 2)
            # speak("According to Wikipedia") 
            print(info)
            speak(info)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'music' in query:
            music_dir = "C:\\Users\\kshah\\OneDrive\\Desktop\\music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'video' in query:
            video1_dir = "C:\\Users\\kshah\\Videos\\Videos"
            videos = os.listdir(video1_dir)
            print(videos)    
            os.startfile(os.path.join(video1_dir, videos[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'single' in query:
            speak(f'yess')
        
        elif 'date' in query:
            speak(f'ofcourse')

        elif 'open vs code' in query:
            codePath = "C:\\Users\\kshah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)













# # import the libraries

# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes

# # so that whatever we pass from our end she can listen and reply to the following
# listener = sr.Recognizer()
# engine = pyttsx3.init()

# # change the voice from male to female
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         talk("Good Morning!")

#     elif hour>=12 and hour<18:
#         talk("Good Afternoon!")   

#     else:
#         talk("Good Evening!")  

#     talk("I am Shahil. Please tell me how may I help you")  


# def talk(audio):
#     engine.say(audio)
#     engine.runAndWait()

# # whatever you pass from your bullshit microphone


# def take_command():

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         command = r.recognize_google(audio, language='en-in')
#         print(f"User said: {command}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return command


# def run_alexa():
#     wishMe()
#     command = take_command().lower()
#     # print(command)
#     if 'play' in command:
#         song = command.replace('play', '')
#         talk('playing' + song)
#         pywhatkit.playonyt(song)

#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         print(time)
#         talk('Current time is'+time)
#     elif 'who is' in command:
#         person = command.replace('who is', '')
#         info = wikipedia.summary(person, 1)
#         print(info)
#         talk(info)
#     elif 'I love you' in command:
#         # person = command.replace('I love you', '')
#         # info = wikipedia.summary(person, 1)
#         # print(info)
#         talk("I love you too!!")

#     elif 'date' in command:
#         talk('sorry, I do not have a pussy')
#     elif 'are you single' in command:
#         talk('No, currently I am doing a gangbang in a room, so sorry I dont want your dick')
#     elif 'joke' in command:
#         talk(pyjokes.get_joke())

# run_alexa()