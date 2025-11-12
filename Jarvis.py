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
import time
import pyjokes
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_MainWindow

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


#To convert text to speech
def speak(audio):
  engine.stop()
  time.sleep(0.1)
  engine.say(audio)
  print(audio)
  engine.runAndWait()



#To wish
def wish():
    time.sleep(0.5)
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good Morning, it's {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon, it's {tt}")
    else:
        speak(f"Good Evening, it's {tt}")
    speak("I am Jarvis sir, please tell me how may I help you")

# if __name__ == "__main__":
#     start()


class MainThread(QThread):
  def __init__(self):
    super(MainThread,self).__init__()

  def run(self):
    self.TaskExecution()

  #To convert voice into text
  def takecommand(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source, timeout=5,phrase_time_limit=10)
    
    try:
      print("Recognizing...")
      self.query = r.recognize_google(audio, language="en-in")
      print(f"User said: {self.query}")

    except Exception as e:
      speak("Say that again please...")
      return "none"
    return self.query

  def TaskExecution(self):
    wish()
    while True:
    # if 1:

      self.query = self.takecommand().lower()

      # logic building for tasks

      if "open notepad" in self.query:
        npath = "C:\\Windows\\notepad.exe"
        os.startfile(npath)

      elif "open command prompt" in self.query:
        os.system("start cmd")

      elif "open camera" in self.query:
        cap = cv2.VideoCapture(0)
        while True:
          ret, img = cap.read()
          cv2.imshow('webcam',img)
          k = cv2.waitKey(50)
          if k == 27:
            break
        cap.release()
        cv2.destroyAllWindows()
      
      elif "play music" in self.query:
        music_dir = "C:\\Users\\HP\\Music"
        songs = os.listdir(music_dir)
        #rd = random.choice(songs)
        for song in songs:
          if song.endswith('.mp3'):
            os.startfile(os.path.join(music_dir,song))
      
      elif "ip address" in self.query:
        ip = get('https://api.ipify.org').text
        speak(f"Your IP address is {ip}")

      elif "wikipedia" in self.query:
        speak("Searching wikipedia...")
        self.query = self.query.replace("wikipedia","")
        results = wikipedia.summary(self.query,sentences = 2)
        speak("According to wikipedia")
        speak(results)
        # print(results)

      elif "open youtube" in self.query:
        webbrowser.open("www.youtube.com")

      elif "open github" in self.query:
        webbrowser.open("https://github.com/")

      elif "open linkedin" in self.query:
        webbrowser.open("linkedin.com/in/harsh-gahlot-b84b85253")

      elif "open google" in self.query:
        speak("Sir, what should I search on google")
        cm = self.takecommand()    
        webbrowser.open(f"{cm}")

      elif "tell me a joke" in self.query:
        joke = pyjokes.get_joke()
        speak(joke)
            
      elif "no thanks" in self.query:
        speak("Thanks for using me sir, have a good day.")
        QApplication.quit()   # ✅ safer exit for PyQt
        break

      
      speak("sir, do you have any other work")



startExecution = MainThread()


class Main(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.startTask)
    self.ui.pushButton_2.clicked.connect(self.close)

  def startTask(self):
    self.ui.movie = QtGui.QMovie("gifi\'s/gifi2.gif")
    self.ui.JarvisUI.setMovie(self.ui.movie)
    self.ui.movie.start()

    self.ui.movie = QtGui.QMovie("gifi\'s/gifi1.gif")
    self.ui.label_2.setMovie(self.ui.movie)
    self.ui.movie.start()
    
    self.ui.movie = QtGui.QMovie("gifi\'s/gifi3.gif")
    self.ui.label_3.setMovie(self.ui.movie)
    self.ui.movie.start()

    timer = QTimer(self)
    timer.timeout.connect(self.showTime)
    timer.start(1000)
    startExecution.start()

  def showTime(self):
    current_time = QTime.currentTime()
    current_date =  QDate.currentDate()
    label_time = current_time.toString('hh:mm:ss')
    label_date = current_date.toString(Qt.ISODate)
    self.ui.textBrowser.setText(label_date)
    self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())













    