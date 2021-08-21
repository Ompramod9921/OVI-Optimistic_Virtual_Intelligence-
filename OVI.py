import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time 
from datetime import datetime
from datetime import date
import randomstuff
import wolframalpha
import winsound
from simple_colors import *
import pyautogui
import pywhatkit

client = wolframalpha.Client('UP5L47-WRARJ3EQ4V')

engine = pyttsx3.init()
engine.setProperty('rate',130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tyme():
    Time = datetime.now().strftime("%H:%M:%S")
    print()
    print(red("Current time is :"))
    print(red(datetime.now().strftime('%X')))
    speak("Current time is")
    speak(Time)

def Date():
    year = int (datetime.now().year)
    month = str (datetime.now().strftime("%B"))
    day = int (datetime.now().day)
    print()
    print(red("Todays date is :"))
    print(red(date.today()))
    speak("Todays date is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) 
    print(red("Welcome back !!!"))
    speak("Welcome back ")
    
    hour = datetime.now().hour
    if hour>=0 and hour<12:
        print(red("Good Morning"))
        speak("Good Morning")
    elif hour>=12 and hour<18:
        print(red("Good Afternoon"))
        speak("Good Afternoon")
    else:
        print(red("Good Evening"))
        speak("Good Evening")

    print(red("ovi at your service. How can i help you"))
    speak("ovi at your service. How can i help you")
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) 

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print()
        print(cyan("Listening..."))
        #r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print(yellow("Recognizing..."))
            query = r.recognize_google(audio,language ='en-in')
            

        except Exception as e:
            print()
            print(magenta("Sorry , could not recognise ..."))
            speak("Sorry , could not recognise ...")
            return ''
        
        return query

def chat():
    with randomstuff.Client(api_key='0nDpRz2FlBRx') as client:
        response = client.get_ai_response(query)
        print()
        print(red(response.message))
        speak(response.message)

if __name__ == "__main__":

    wishme() 

    while True :
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            tyme()

        elif "date" in query:
            Date()

        elif "good bye" in query or "ok bye" in query or "stop" in query:
            print()
            print(red('your personal assistant ovi is shutting down . Good bye'))
            speak('your personal assistant ovi is shutting down . Good bye')
            quit()

        elif "wikipedia" in query:
            print()
            print(cyan("searching..."))
            speak("searching...")
            query = query.replace("wikipedia" ,"")
            result = wikipedia.summary(query, sentences=2)
            print(red("According to wikipedia"))
            speak("According to wikipedia")
            print()
            print(red(result))
            speak(result)

        elif 'open youtube' in query:
            print()
            print(red("Opening youtube..."))
            speak("opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(5)

        elif 'open google' in query:
            print()
            print(red("Opening google..."))
            speak("opening Google")
            webbrowser.open_new_tab("https://www.google.com")
            time.sleep(10)

        elif 'open gmail' in query:
            print()
            print(red("Opening gmail..."))
            speak("opening Gmail")
            webbrowser.open_new_tab("gmail.com")
            time.sleep(10)
        
        elif 'who are you' in query or 'what can you do' in query:
            print()
            print(red('I am ovi version 1.0 your persoanl assistant. I am programmed to do minor tasks like '
                  'opening youtube,google chrome,gmail ,predict time, sending whatsapp message, search wikipedia, predict weather ' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!'))
            speak('I am ovi version 1 point 0 ...your persoanl assistant . I am programmed to do minor tasks like '
                  'opening youtube ,google chrome,gmail, predict time, sending whatsapp message, search wikipedia, predict weather ' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            print()
            print(red("I was built by omkar and vivek"))
            speak("I was built by omkar and vivek")

        elif 'news' in query:
            print()
            print(red("Here are some headlines from the Times of India,Happy reading"))
            speak('Here are some headlines from the Times of India ....Happy reading')
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            time.sleep(10)

        elif 'search' in query:
            query = query.replace("search", "")
            print()
            print(red("Searching..."))
            speak("searching...")
            webbrowser.open_new_tab(query)
            time.sleep(10)

        elif 'ask' in query:
            query = query.replace("ask" ,"")
            res = client.query(query)
            output = next(res.results).text
            print()
            print(red(output))
            speak(output)

        elif 'game' in query :
            print()
            print(red("launching game..."))
            speak("launching game...")
            from freegames import flappy
            time.sleep(5)

        elif "whatsapp" in query :
            print()
            print(red("whom you want to send message  "))
            speak("whom would you like to send message" )
            person_name = takeCommand()
            print(person_name)
            print()
            print(red("what is your message : "))
            speak("what is your message ")
            msg = takeCommand()
            print(msg)
            print()
            print(red("Sending message on whatsapp..."))
            speak("Sending message on whatsapp...")
            webbrowser.open('https://web.whatsapp.com/')
            time.sleep(12)
            #click on search bar
            pyautogui.click(296,281)
            pyautogui.typewrite(person_name)
            time.sleep(5)
            #click on the person
            pyautogui.click(238,444)
            time.sleep(5)
            #click on typying box
            pyautogui.click(898,1017)
            pyautogui.typewrite(msg)
            time.sleep(2)
            #sending msg
            pyautogui.click(1791,1016)
            time.sleep(4)
            #return back
            pyautogui.click(1774,19)
            print()
            print(red("message sent..."))
            speak("message sent ...")

        elif "song" in query:
            music = query.replace("song",'')
            print()
            print(red("playing song...."))
            speak("playing song....")
            pywhatkit.playonyt(music)
            time.sleep(12)

        elif "image" in query:
            with randomstuff.Client(api_key='0nDpRz2FlBRx') as client:
                image = client.get_image(type="any")
                print()
                print(red("taking you to the image..."))
                speak("taking you to the image...")
                webbrowser.open_new_tab(image)
                time.sleep(5)

        else:
            chat()