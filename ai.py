import pyttsx3
import speech_recognition as sr
import datetime
from datetime import timedelta
import os
import cv2
import random
import sys
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import webbrowser
import PyPDF2
import wikipedia
import pywhatkit as kit
from pywikihow import search_wikihow
import psutil
import speedtest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 250)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry sir, can you say it again?")
        return "none"
    except sr.RequestError as e:
        speak(f"Error: {e}")
        return "none"

speak("Please wait before speaking, it might take a while to load. Speak once it shows this text 'Listening....'. Thank you")

def wish():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 0 <= hour < 12:
        speak(f"Good Morning! It is {current_time:%I:%M %p}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon! It is {current_time:%I:%M %p}")
    else:
        speak(f"Good Evening! It is {current_time:%I:%M %p}")
    speak("I am Jarvis. Please tell me how can I help you.")

def search_web(query):
    try:
        search_url = f"https://www.google.com/search?q={query}"

        response = requests.get(search_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            answer_element = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
            if answer_element:
                return answer_element.text
    except Exception as e:
        print("Error:", e)
    return None

def answer_question(question):
    speak("Let me find the answer to that question.")
    answer = search_web(question)
    if answer:
        speak(f"The answer to your question is: {answer}")
    else:
        speak("Sorry, I couldn't find an answer to your question.")
        
def get_location():
    try:
        ip_address = requests.get("https://api.ipify.org").text
        response = requests.get(f"https://get.geojs.io/v1/ip/geo/{ip_address}.json")
        geo_data = response.json()
        city = geo_data.get("city")
        country = geo_data.get("country")
        return city, country
    except Exception as e:
        speak("Sorry sir, I was unable to find where we are.")
        return None, None

def get_temperature(city):
    try:
        search = f"temperature in {city}"
        url = f"https://www.google.com/search?q={search}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        temperature = soup.find("div", class_="BNeawe").text
        return temperature
    except Exception as e:
        speak("Sorry sir, I couldn't fetch the current temperature.")
        return None

def pdf_reader():
    pdf = input("Please enter the file name (do not include extension): ")
    book = open(f"{pdf}.pdf","rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Please enter the page number I have to read.")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

last_command = ""

def TaskExecution():
    wish()
    while True:
        query = takecommand()
        
        if query == "none":
            continue
        
        if query == "repeat":
            query = last_command
        
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            
        elif "open command prompt" in query:
            os.system("start cmd")
            
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(20)
                if k==10:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            
        elif "play" and "media" in query:
            music_dir = "C:\\Users\\Om\\OneDrive\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        
        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")
        
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia,")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There were multiple matches for your query. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I could not find any information on that topic.")
        
        elif "time" in query:
            current_time = datetime.datetime.now()
            speak(f"The current time is {current_time:%I:%M %p}")
            
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today's date is {current_date}")
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open powerpoint" in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        
        elif "open google" in query:
            speak("What should I search?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "open gmail" in query:
            speak("Which account should I open?")
            acc = input("Please enter the gmail account you want me to open (enter @gmail.com as well):")
            webbrowser.open(f"https://mail.google.com/a/{acc}")
            
        elif "play" in query and "youtube" in query:  
            speak("What should I play?")
            yt = takecommand().lower()
            kit.playonyt(yt)
        
        elif "play" and "spotify" in query:
            webbrowser.open("https://open.spotify.com/?flow_ctx=9013b08b-4cff-4c2b-b8ad-67b9a9ccb126%3A1718260298")
        
        elif "shut down" and "system" in query:
            os.system("shutdown /s /t 5")
        
        elif "restart" and "system" in query:
            os.system("shutdown /r /t 5")
        
        elif "sleep" and "system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
        elif "switch" and "window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif "details" in query:
            speak("Wait sir, let me go through them. What do you want to know?")
            newquery = takecommand()
            if "age" in newquery:
                speak("What is your birthdate?")
                birthdate = takecommand()
                birthdate = datetime.strptime(birthdate, '%d-%m-%Y')
                today = datetime.today()
                years = today.year - birthdate.year
                months = today.month - birthdate.month
                days = today.day - birthdate.day

                if days < 0:
                    months -= 1
                    previous_month = today.replace(day=1) - timedelta(days=1)
                    days += previous_month.day
                elif months < 0:
                    years -= 1
                    months += 12

                age = {"years": years, "months": months, "days": days}
                speak(age)
                
            if "education" and "number" in newquery:
                speak("Sir, your Ontario Education Number is 538178211.")
            
            if "birthdate" in newquery:
                speak("Sir your birthdate is 31 August and the year is 2009.")
            
        elif ("where" in query and "am" in query) or "location" in query:
            speak("Wait sir, let me check.") 
            city, country = get_location()
            if city and country:
                speak(f"Sir, I think we are in {city} city of {country}.")
        
        elif "screenshot" in query:
            speak("Sir, please tell me the name for this screenshot file.")
            name = takecommand().lower()
            speak("Please hold the screen for a few seconds. I am taking screenshot.")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done, sir. The screenshot has been saved in the main folder.")
        
        elif "score" and "cricket" in query:
            webbrowser.open("https://www.google.com/search?q=live+cricket+score&sca_esv=421b6f880c88a314&sca_upv=1&sxsrf=ADLYWIIf6eUNSNCXoUtcKr7Qm3F3nn2l5Q%3A1718233886234&ei=HitqZqLzDeafptQPrJe26Ag&ved=0ahUKEwii-reDmNeGAxXmj4kEHayLDY0Q4dUDCBA&uact=5&oq=live+cricket+score&gs_lp=Egxnd3Mtd2l6LXNlcnAiEmxpdmUgY3JpY2tldCBzY29yZTIREAAYgAQYkQIYsQMYgwEYigUyERAAGIAEGJECGLEDGIMBGIoFMhEQABiABBiRAhixAxiDARiKBTIIEAAYgAQYsQMyBhAAGAcYHjILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAESPckUPwQWIsicAN4ApABAJgBvwGgAfEJqgEEMC4xMLgBA8gBAPgBAZgCDaACswnCAgQQABhHwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAhkQLhiABBiwAxjRAxhDGMcBGMgDGIoF2AEBwgIHECMYsQIYJ8ICBxAjGLACGCfCAgcQABiABBgNwgIGEAAYAxgNwgIKEAAYgAQYsQMYDcICDRAAGIAEGLEDGIMBGA3CAhAQABiABBixAxiDARiKBRgNmAMAiAYBkAYMugYECAEYCJIHAzQuOaAHg0I&sclient=gws-wiz-serp#cobssid=s")
        
        elif "score" and ("soccer" or "football") in query:
            webbrowser.open("https://www.livescore.com/en/")
            
        elif "read pdf" in query:
            pdf_reader()
        
        elif "how are you" in query:
            speak("I am fine, sir. How are you?")
            response = takecommand()
            if "fine" in response or "good" in response or "also good" in query:
                speak("That is good to hear.")
        
        elif "you can sleep" in query:
            speak("Okay, sir. I am going to sleep. Please call me whenever you want.")
            break
        
        elif "temperature" or "weather" in query:
            city, _ = get_location()
            if city:
                temperature = get_temperature(city)
                if temperature:
                    speak(f"The current temperature in {city} is {temperature}")
        
        elif "activate how to do mode" in query:
            speak("how to do mode is activated.")
            while True:
                speak("Please tell me what you want me to know.")
                how = takecommand()
                try:
                    if "exit" or "close" in how:
                        speak("okay, sir. How to do mode is closed.")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry, sir! I am not able to do this.")
        
        elif "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir, the battery percentage is {percentage}")
        
        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            dlmb = dl/1000000
            rounded_dlmb = round(dlmb, 0)
            up = st.upload()
            upmb = up/1000000
            rounded_upmb = round(upmb, 0)
            speak(f"Sir, the download speed is {rounded_dlmb} Mb per second and upload speed is {rounded_upmb} Mb per second.")
        
        elif "hey Jarvis" in query:
            answer_question(query)

        elif "bye" in query:
            speak("Goodbye, sir. Have a great day!")
            sys.exit()
        
if __name__ == "__main__":
    TaskExecution()