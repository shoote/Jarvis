import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

#To convert text to speech
def speak(audio):
  engine.say(audio)
  print(audio)
  engine.runAndWait()

#To convert voice into text
def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source, timeout=5,phrase_time_limit=10)
  
  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language="en-in")
    print(f"User said: {query}")

  except Exception as e:
    speak("Say that again please...")
    return "none"
  return query

#To wish
def wish():
  hour =int(datetime.datetime.now().hour)

  if hour >= 0 and hour <=12:
    speak("Good Morning")
  elif hour > 12 and hour < 18:
    speak("Good Afternoon")
  else:
    speak("Good Evening")
  speak("I am Jarvis sir, please tell me how can I help you")

if __name__ == "__main__":
  wish()
  while True:
  # if 1:

    query = takecommand().lower()

    # logic building for tasks

    if "open notepad" in query:
      npath = "C:\\Windows\\notepad.exe"
      os.startfile(npath)

    elif "open command prompt" in query:
      os.system("start cmd")

    elif "open camera" in query:
      cap = cv2.VideoCapture(0)
      while True:
        ret, img = cap.read()
        cv2.imshow('webcam',img)
        k = cv2.waitKey(50)
        if k == 27:
          break
      cap.release()
      cv2.destroyAllWindows()
    
    elif "play music" in query:
      music_dir = "C:\\Users\\HP\\Music"
      songs = os.listdir(music_dir)
      #rd = random.choice(songs)
      for song in songs:
        if song.endswith('.mp3'):
          os.startfile(os.path.join(music_dir,song))
    
    elif "ip address" in query:
      ip = get('https://api.ipify.org').text
      speak(f"Your IP address is {ip}")

    elif "wikipedia" in query:
      speak("Searching wikipedia...")
      query = query.replace("wikipedia","")
      results = wikipedia.summary(query,sentences = 2)
      speak("According to wikipedia")
      speak(results)
      # print(results)

    elif "open youtube" in query:
      webbrowser.open("www.youtube.com")

    elif "open github" in query:
      webbrowser.open("https://github.com/")

    elif "open linkedin" in query:
      webbrowser.open("linkedin.com/in/harsh-gahlot-b84b85253")

    elif "open google" in query:
      speak("Sir, what should I search on google")
      cm = takecommand().lower()
      webbrowser.open(f"{cm}")
           
    elif "no thanks" in query:
      speak("thanks for using me sir, have a good day.")
      sys.exit()
    
    speak("sir, do you have any other work")
    