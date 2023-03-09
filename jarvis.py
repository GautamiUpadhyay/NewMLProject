import pyttsx3 
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")   

    speak("I am jarvis  Sir please tell me How may  I help you ")
def takeCommand():

    r = sr.Recogniser() 
    with sr.Microphone as Source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(Source)
    try:
        

if __name__ == "__main__":
    wishme()
 