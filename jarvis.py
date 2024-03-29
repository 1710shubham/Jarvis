import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
     
    elif hour>=12 and hour<18:   
        speak("Good AfterNoon!")

    else:
        speak("Good Evening!")
        
    
    speak("I am Jarvis Sir. Kese hai App log!")

def takeCommand():
    #it takes microphone input from the user and returns string output

   r = sr.Recognizer()
   with sr.Microphone() as source: 
       print("Listening...")
       r.pause_threshold = 1
       audio = r.listen(source)
       
   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language="en-IN")
       print(f"User said: {query}\n")       
       
   except Exception as e: 
       #print(e)
       print("Say that Agin please...")
       return "None"
   return query
   
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
      query = takeCommand().lower()

      #Logic for executing tasks based on query
      if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

      elif 'open youtube' in query:
          webbrowser.open("youtube.com")

      elif  'open whatsapp' in query:
          webbrowser.open("https://web.whatsapp.com/")

      elif  'open google' in query:
          webbrowser.open("google.com")

      elif  'sabse badi khushi' in query:
          webbrowser.open("https://www.youtube.com/shorts/cbjZE6nG2yc")
      
      elif  'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
    
      elif 'open vs code' in query:
          codePath = "C:\\Users\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)

      elif 'play music' in query:
          codePath1 = "C:\\Users\\HP\\Desktop\\Shubham\\JARVIS\\shoorveer_3.mp3"
          os.startfile(codePath1)

       

      