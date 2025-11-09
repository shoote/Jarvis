import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

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
    audio = r.listen(source, timeout=1,phrase_time_limit=5)
  
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

  

if __name__ == "__main__":
  takecommand()
  # speak()