import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil



engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

newVoiceRate= 165
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("It's about")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
    
def wishMe():
    speak(",")
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good morning darrshan")
    elif hour>12 and hour<=17:
        speak("Good Afternoon darrshan")
    elif hour>17 and hour<=21:
        speak("Good Evening darrshan")
    else:
        speak("Hello darrshan")

    speak("Alis at your service . HOw can I help you?")

def Love():
    speak("I am only your's my love,")

def mom():
    speak("Namaste aee, how are you?")
    speak("I mean. kase ahat")
def cobra():
    speak("Aditya AKA Toxic cobra is the coleader of team LOC esoports ")
    speak("He is still single")

def breakup():
    speak("ohh come on darrshan . i am ever ready for a break up. dude.but nobody is going to stay with you after me")
    speak("so think about it before asking , ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en=IN')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    
    return query

def sendmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("therupalichaudhari199@gmail.com","8329367980")
    server.sendmail("therupalichaudhari199@gmail.com",to,content)
    server.close()
def codechef():
    speak("runtime terror is a group of few enthusiastic students of SGGS institute and it has leaded by Gauri katti")
def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\Alis\ss.png")
def cpu():
    usage= str(psutil.cpu_percent())
    speak("CPU is at"+ usage)

    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.precent)

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Okay, I will not disturb you any more")
            quit()
        elif "who are you" in query:
            Love()
        elif "send email" in query:
            try:
                speak("yeah sure, but What should I say?")
                content = takeCommand()
                to="2020bit029@sggs.ac.in"
                sendmail(to, content)
                speak("done, Email sent successfully")
            except:
                speak("ohh sorry ,i am not able to send the mail ")

                
        elif "wikipedia" in query:
            speak("Just a second, searching...")
            query= query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif "browser" in query:
            speak("What should I search?")
            browserpath = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
            search=takeCommand().lower()
            wb.get(browserpath).open_new_tab(search + ".com")
        elif "shut down computer" in query:
            os.system("shutdown /s /t 1")
        elif "restart computer" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir="E:\Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember" in query:
            speak("okay, go on")
            data=takeCommand()
            speak("You said me to remember"+ data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember= open("data.txt", "r")
            speak("You said me to remember this "+ remember.read())
        
        elif "cpu" in query:
            cpu()

        elif "break up" in query:
            breakup()
        elif "mother" in query:
            mom()
        elif "cobra" in query:
            cobra()
        elif "code" in query:
            codechef()
             
                
                            
            
