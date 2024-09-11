import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from random import randint
from random import random
import requests
from bs4 import BeautifulSoup
import pyautogui
from time import sleep


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning boss")
    elif hour>=12 and hour<18:
        speak("good afternoon boss")
    else:
        speak("good evening boss")
    speak("i am chetan . your personalized A,I voice assistant . how may i help you boss")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
 

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")   

        elif 'open stackoverflow' in query: 
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"boss, the time is {strTime}")   
        
        elif 'open spotify web' in query:
            webbrowser.open("spotify.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open xhamster' in query:
            webbrowser.open("xhamster19.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[randint(0,21)]))

        

        elif 'open notepad' in query:
            os.startfile('C:\\Windows\\System32\\notepad.exe')

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            os.system("start microsoft.windows.camera:")


        elif 'open calculator' in query:
            os.system("start calc:")


        elif 'open paint' in query:
            os.system("start mspaint:")


        elif 'open word' in query:
            os.system("start winword:")

        elif 'open spotify' in query:
            os.system("start spotify:")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"boss, the time is {strTime}")  


        elif 'stop' in query:
            exit()

        
        elif 'weather' in query:
        

            search = "weather in kolkata"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")


        elif 'pause' in query:
            pyautogui.hotkey('playpause')
            speak('video paused')


        elif 'play' in query:
            pyautogui.hotkey('playpause')
            speak('video played')

        elif 'mute' in query:
            pyautogui.hotkey('m')
            speak ('video muted')


        elif "volume up"  in query:
            from keyboard import volumeup
            speak("turning volume up by 5 , boss")
            volumeup()

        elif "volume down" in query:
            from keyboard import volumedown
            speak("turning volume down by 5 , boss")
            volumedown()


        


            
        

        



          

        



