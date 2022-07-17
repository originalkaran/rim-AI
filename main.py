import pyttsx3    #pip install pyttsx3
import speech_recognition as sr   #pip install speechRecognition
import datetime
import pyaudio
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
from pathlib import Path

filepath = Path(r"C:\Users\Karan raj\vs code\pass.txt")

with open(filepath, 'r') as f:
    password = f.readline()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """
    Greets the user and tell about itself.
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        morning = "Good morning karan!"
        print(morning)
        speak(morning)        
    elif hour >= 12 and hour < 18:
        afternoon = "Good afternoon karan!"
        print(afternoon)
        speak(afternoon)
    else:
        evening = "Good evening Karan!"
        print(evening)
        speak(evening)
    intro = "I am Rim, please tell me how can i help you Karan!"
    print(intro)
    speak(intro)


def takeCommand():
    """
    Takes input from user in microphone and returns output in string.
    """
    r = sr.Recognizer()         #this class helps us to recognize the audio.
    with sr.Microphone() as source:
        print("Listening....")
        #r.pause_threshold = 1
        #print("abc")
        #r.energy_threshold = 350
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:    #if any error occured while recognizing.
        print(e)
        print("say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    """ Sends email to specified person."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('karan.raj.1101@gmail.com', password)
    server.sendmail('karan.raj.1101@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    while True:
        query = takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open mail' in query:
            webbrowser.open("mail.google.com")

        elif 'open udemy' in query:
            webbrowser.open("udemy.com")

        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open movies' in query:
            movies_dir = 'D:\\movies'
            os.startfile(movies_dir)

        elif 'open my programs' in query:
            vscode_dir = 'C:\\Users\\Karan raj\\vs code'
            os.startfile(vscode_dir)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir The time is {strTime}")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\Karan raj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif "repeat after me" in query:
            query = query.replace("repeat after me","")
            speak(query)
        
        elif 'Hey bhagwan' in query:
            speak("What happened Karan! Bhagwan tumhare sath hai!")
        
        elif 'send email to karan' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "rajkaran208@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend karan. I was not able to send email.")