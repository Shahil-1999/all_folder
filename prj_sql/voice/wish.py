import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import os
import voice.speak as sp

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        sp.speak("Good Morning!")

    elif hour>=12 and hour<18:
        sp.speak("Good Afternoon")

    else:
        sp.speak("Good Evening")