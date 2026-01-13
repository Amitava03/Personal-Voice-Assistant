import webbrowser
import speech_recognition as sr
import pyttsx3
import musicLibrary
import pygame
import os
from google import genai
from google.genai import types
from gtts import gTTS


recognizer = sr.Recognizer() 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Set to a specific voice
geminiapi = "AIzaSyC_vt94zn12zTsEoteabG8cETWpkQJxsFs"


def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save('temp.mp3')
    
    
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    

    
def aiProcess(command):
    client = genai.Client(api_key="AIzaSyC_vt94zn12zTsEoteabG8cETWpkQJxsFs")
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=command,
    config=types.GenerateContentConfig(
        system_instruction="You are a virtual assistant named Jarvis skilled in general tasks like google and alexa"
    )
)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://www.google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
          
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif c.lower().startswith("news"):
        webbrowser.open("https://news.google.com")
        speak("Opening Google News")
        
    elif c.lower().startswith("weather"):
        webbrowser.open("https://www.weather.com")
        speak("Opening Weather Forecast")
        
    elif c.lower().startswith("search for"):
        query = c.lower().split("for",1)[1]
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google")
        
    else:
        #Let AI handle it
        output = aiProcess(c)
        speak(output)
         

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=10)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
            elif "stop" in command.lower():
                speak("Okay! Goodbye")
                break
                          
        except Exception as e:
            print("Error; {0}".format(e))
            

            