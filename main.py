import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser


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
        speak("Good morning karan!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Karan!")
    else:
        speak("Good evening!")
    speak("I am Rim, please tell me how can i help you Karan!")

def takeCommand():
    """
    Takes input from user in microphone and returns output in string.
    """
    r = sr.Recognizer()         #this class helps us to recognize the audio.
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
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


if __name__ == "__main__":
    wishMe()
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
