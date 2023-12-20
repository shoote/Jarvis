import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser 
import sys
import time
import pyjokes
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore  import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
        
    
    if hour>=0 and hour<12:
        speak(f"Good Morning!, its {tt}, I am jarvis sir. please tell me how may i help you")

            
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!, its {tt}, I am jarvis sir. please tell me how may i help you")

            
    else:
        speak(f"Good Evening!, its {tt}, I am jarvis sir. please tell me how may i help you")



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution()
        
    def takecommand(self): 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            #audio = r.listen(source,timeout=5,phrase_time_limit=5)
            
            
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            
        except Exception as e:
            speak("Say that again please...")
            return "none"
        query = query.lower()
        return query

    
    def TaskExecution(self):   
     if __name__ == "__main__":
        wish()
        while True:
        # if 1:
        
            
            self.query = self.takecommand()
    
            # logic building for tasks
            
# to open notepad
            if "open notepad" in self.query:
                npath = "C:\\windows\\system32\\notepad.exe"
                os.startfile(npath)
                speak("opening notepad")
                
# to open command prompt
            elif "open command prompt" in self.query:
                os.system("start cmd")
                speak("opening command prompt")

# to open camera                
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
                
                
# to tell a joke
            elif "tell a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
                
                    
# to play music
            elif "play music" in self.query:
                music_dir= "D:\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("playing music")
                
# to tell the IP address
            elif "what is my ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
                
# to search wikipedia
            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)
               
# to open youtube
            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")

# to open youtube                
            elif "open spotify" in self.query:
                webbrowser.open("www.spotify.com")
                speak("opening spotify")
                
# to open stackoverflow
            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")
                speak("opening stackoverflow")
                
# to search google
            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
                speak("your result is")
                
            elif "no thanks" in self.query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()
                
            speak("sir do you want any other work")
            


startExecution = MainThread()





           
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\\jarvis\\gui\\7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\\jarvis\\gui\\jarvis-gif-6.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())