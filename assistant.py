import tkinter as tk
import speech_recognition as sr
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
import pyttsx3
import wikipedia
import re
import datetime
import webbrowser
import os
import json
import time
from bs4 import BeautifulSoup
from time import sleep
import subprocess
import keyboard
from ecapture import ecapture as ec
import random
import requests
import threading



def run_voice_assistant():
    threading.Thread(target=voice_assistant).start()

def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data

# Save user data to file
def save_user_data(user_data):
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)


user_data = load_user_data() 

def speak(text):
    global user_data 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 166)
    engine.say(text)
    engine.runAndWait()


import speech_recognition as sr

def get_user_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.dynamic_energy_adjustment_ratio = 1.5  # Increase sensitivity to low-volume input
        r.dynamic_energy_adjustment_damping = 0.15  # Reduce damping time for faster adjustment
        recorded_audio = None  # Initialize recorded audio as None
        while recorded_audio is None:  # Continue listening until audio is captured
            try:
                recorded_audio = r.listen(source, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                print("Timeout. Continue speaking to provide your command...")
        
    try:
        user_input = r.recognize_google(recorded_audio, language='en-IN')
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your voice.")
        return ""
    except sr.RequestError as e:
        print("Sorry, there was an error with the voice recognition service.")
        return ""

def speak_current_date():
    current_date = datetime.date.today().strftime("%B %d, %Y")
    speak("Today's date is " + current_date)

import subprocess

def open_chrome():
    # Open Chrome using the 'start' command on Windows
    subprocess.Popen(['start', 'chrome'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def voice_assistant():
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    trigger_words = ['assistant','hey chitthi','hello chitthi','hey chitti','hello chitti','50','cheating','city','citi','chitti','chitthi','preeti','priti','chite','vt','svt','hey svt','hey preeti','priti','siri','varsha']

    
    while True:
        statement = get_user_input().lower()
        print("You said:", statement)

        if any(trigger_word in statement for trigger_word in trigger_words):
            tokens = word_tokenize(statement)
            tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
            tokens = [token for token in tokens if token not in stop_words]
            for word in trigger_words:
               if word in statement:
                   statement = statement.replace(word, "")
                   statement = statement.strip()
            a=statement
            user_data = load_user_data()
            window=tk.Tk()
    
            if any(word in tokens for word in ['goodbye', 'bye','bhai']):
                responses = [
                            "Goodbye! Have a great day!",
                            "Bye bye! Take care and see you soon!",
                            "Farewell! Until we meet again!",
                            "Take care! Remember, I'm here whenever you need assistance!",
                            "Goodbye! It was a pleasure helping you!",
                            "Bye for now! Stay safe and happy!",
                            "Take care! Don't hesitate to reach out if you need anything!",
                            "Goodbye! May your day be filled with joy and success!",
                            "Bye bye! Remember, I'm just a call away!",
                            "Farewell! Wishing you all the best!",
                            "Goodbye! Don't forget, I'm here to make your life easier!",
                            "Bye for now! Stay positive and keep smiling!",
                            "Take care! I'll be eagerly waiting for your next interaction!",
                            "Goodbye! Make the most of every moment!",
                            "Bye bye! Take some time for yourself and relax!"
                    ]
                response = random.choice(responses)
                print("Chitti :"+response)
                speak(response)
               
            elif any(word in tokens for word in ['hi', 'hello']):
                responses = [
                    "Hi there!",
                    "Hello! How can I assist you today?",
                    "Hey! What can I do for you?",
                    "Greetings! How may I help you?",
                    "Hello! I'm here to answer your questions!",
                    "Hi! How may I be of service?",
                    "Hey there! What brings you here?",
                    "Hello! Feel free to ask anything you'd like!",
                    "Hi! It's nice to see you!",
                    "Hello! I hope you're having a great day!",
                    "Hey! Is there anything specific you need help with?",
                    "Hi! How can I make your day better?",
                    "Hello! Let's get started. What do you need assistance with?",
                    "Hi there! I'm ready to assist you. What can I do for you today?",
                    "Hello! I'm here to provide the answers you're looking for!",
                    "Hi! Tell me how I can assist you and I'll do my best!",
                    "Hello! I'm all ears. What can I help you with?",
                    "Hi! I'm at your service. What can I help you with today?",
                    "Hello! I'm here to make your life easier. How can I assist you?"
                ]
                response = random.choice(responses)
                print("Chitti: " + response)
                speak(response)

            elif 'how are you'in statement or 'what about you' in statement:
                responses = [
                    "I'm an AI language model, so I don't have feelings, but thank you for asking! How can I help you today?",
                    "I'm here and ready to assist you! How can I be of service?",
                    "Thank you for asking! I'm always ready to help. How can I assist you today?",
                    "I'm doing well in my virtual world! How may I assist you today?",
                    "As an AI, I'm always ready to help! How can I make your day better?",
                    "I'm functioning perfectly! How may I assist you?",
                    "Thanks for asking! I'm at your service. How can I help you today?",
                    "I'm here and eager to assist you! How can I contribute to your success?",
                    "Thank you for your concern! I'm here to provide you with exceptional service. How may I assist you today?",
                    "I'm doing great, ready to assist you! How can I make your experience amazing?",
                    "I'm ready to help you out! How can I make your life easier today?",
                    "I'm doing well! How can I simplify things for you today?",
                    "Thanks for asking! I'm here to be your reliable assistant. How can I assist you today?",
                    "I'm functioning flawlessly! How can I exceed your expectations?",
                    "Thank you for asking! I'm here to bring a smile to your face. How may I assist you today?",
                    "I'm doing fantastic! How can I make your day brighter?",
                    "I'm here and ready to assist you! How can I make your experience extraordinary?",
                    "Thank you for your concern! I'm here to make your life easier. How can I assist you today?",
                    "I'm doing well! How can I simplify things for you?",
                    "Thanks for asking! I'm here to be your reliable assistant. How can I contribute to your success?"
                ]
                response = random.choice(responses)
                print("Chitti: " + response)
                speak(response)
                

            elif any(word in tokens for word in ['good','iam fine','im fine','im good','im good thanks for asking','help','help me','why you are here','why are you here','i need help','i know you can help me','i want you','i need you']):
                response = "i love to here it , I'm here to help. What do you need assistance with?"
                print("Chitti :"+response)
                speak(response)

            elif any(word in tokens for word in ['you are mine', 'i love you ','love you','you are great', 'you are the best assistant ', 'i like you', 'great work','perfect']):
                response = "Thanks,I love to here it, I'm here to help. What do you need assistance with?"
                print("Chitti :"+response)
                speak(response)

            elif any(word in tokens for word in ['thank', 'tanks','thans']):
                responses = [
                    "You're welcome!",
                    "No problem!",
                    "Glad I could help!",
                    "My pleasure!",
                    "Anytime!",
                    "I'm here to assist!",
                    "You're most welcome!",
                    "I'm glad I could be of assistance!"
                ]
                response = random.choice(responses)
                speak(response)
                print("Chitti :"+response)
            
            elif any(word in tokens for word in ['time', 'current']):
                import datetime
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                response = "The current time is {current_time}."
                speak(response)
                print("Chitti: " + response)
            
            elif "date" in statement:
                speak_current_date()
            elif 'remember my bio' in statement:
                speak("chitti: Sure! What's your name?")
                print("chitti: Sure! What's your name?")
                name_input = get_user_input()
                user_data['name'] = name_input
                save_user_data(user_data)
                speak("I've remembered your name as " + name_input)
                print("Chitti: I've remembered your name as", name_input)

                speak(f"chitti: How old are you {user_data['name']}?")
                print(f"chitti: How old are you {user_data['name']}?")
                age_input = get_user_input()
                age_ = re.sub(r'\D', '', age_input)
                user_data['age'] = age_
                save_user_data(user_data)

                if int(age_) > 18:
                    speak("chitti: Are you in a relationship? Reply with Yes or No")
                    print("chitti: Are you in a relationship? Reply with Yes or No")
                    lov_input = get_user_input()

                    if lov_input.lower() == 'yes':
                        speak("I'm eagerly waiting to hear that lucky girl's name")
                        lov = get_user_input()
                        lov = lov.replace("she is", "").replace("her name is", "").strip()
                        user_data['love'] = lov
                        save_user_data(user_data)
                        speak("It's a cute name")
                    else:
                        speak("It's fine, I'm single too...")

                    speak(f"chitti: What is your favorite food, {user_data['name']}?")
                    print(f"chitti: What is your favorite food, {user_data['name']}?")
                    food_input = get_user_input()
                    user_data['food'] = food_input
                    save_user_data(user_data)
                    speak("I love it too...")

                    speak(f"chitti: What is your favorite place, {user_data['name']}?")
                    print(f"chitti: What is your favorite place, {user_data['name']}?")
                    place_input = get_user_input()
                    user_data['place'] = place_input
                    save_user_data(user_data)

                    speak(f"{user_data['name']}, I will remember you till my last breath")


            elif "what is my name" in statement:
                if 'name' in user_data:
                    response = f"Your name is {user_data['name']}."
                else:
                    response = "I'm sorry, I don't know your name. Could you please tell me?"
            elif "what is my age" in statement:
                if 'age' in user_data:
                    response= f"your age is {user_data['age']}."
                else :
                    response = "i am sorry , I don't know your age. could you please tell me?"


            elif "i need your assistance" in statement or "i need help" in statement:
                response = "Thanks,I love to here it, I'm here to help. What do you need assistance with?"
                speak(response)
                print("Chitti :"+response)
            
            elif "send a message in whatsapp" in statement:
                import pyautogui
                speak('To whom are you going to send a message')
                recipient = get_user_input().lower()
                speak('speak your message')
                message = get_user_input().lower()
                pyautogui.press('win')
                sleep(1)
                pyautogui.click(x=780, y=81)
                txt = "Whatsapp"
                keyboard.write(txt)
                keyboard.press('enter')
                sleep(4)
                pyautogui.click(x=158, y=124)
                sleep(1)
                keyboard.write(recipient)
                sleep(2)
                pyautogui.click(x=226, y=209)
                sleep(2)
                pyautogui.click(x=616,y=741)
                sleep(2)
                pyautogui.typewrite(message)
                keyboard.press('enter')
                sleep(4)
                speak('message sent')
                pyautogui.hotkey('alt','F4')

            
            elif 'send a message in telegram' in statement:
                import pyautogui
                speak('To whom are you going to send a message')
                recipient = get_user_input()
                print(recipient)
                speak('speak your message')
                message = get_user_input()
                pyautogui.press('win')
                sleep(1)
                pyautogui.click(x=780, y=81)
                txt = "telegram"
                keyboard.write(txt)
                keyboard.press('enter')
                sleep(4)
                pyautogui.click(x=121, y=50)
                keyboard.write(recipient)
                sleep(1)
                pyautogui.click(x=175, y=109)
                sleep(1)
                pyautogui.typewrite(message)
                keyboard.press('enter')
                speak('message sent')
                pyautogui.hotkey('alt','F4')

            elif "shutdown" in statement or "switch off" in statement:
                speak("Shutting down , bye")
                import pyautogui
                pyautogui.hotkey('win','x')
                sleep(1)
                pyautogui.press('u')
                pyautogui.press('u')
                
            
            elif "go to sleep" in statement or "sleep" in statement:
                speak("Ok , sleep Mode On")
                import pyautogui
                pyautogui.hotkey('win','x')
                sleep(1)
                pyautogui.press('u')
                pyautogui.press('s')

            elif "restart" in statement or "reboot" in statement:
                speak(f"Ok , {user_data['name']} ")
                import pyautogui
                pyautogui.hotkey('win','x')
                sleep(1)
                pyautogui.press('u')
                pyautogui.press('r')

            elif "screenshot" in statement:
                import pyautogui 
                im = pyautogui.screenshot()
                im.save("ss.jpg") 
                speak('  done')

            elif 'minimize' in statement or 'minimise' in statement:
                speak('  sure')
                import pyautogui
                pyautogui.hotkey('win','d')
                speak('  done')

            elif 'undo' in statement:
                import pyautogui
                pyautogui.hotkey('ctrl','z')
                speak('done')
            

            elif 'close' in statement or 'quit' in statement or 'end' in statement :
                import pyautogui
                pyautogui.hotkey('alt','F4')
                speak('done')
                
            elif 'go back' in statement or 'switch' in statement:
                speak('sure')
                import pyautogui
                pyautogui.hotkey('alt','tab')
                speak('done')

            elif 'select all' in statement:
                import pyautogui
                pyautogui.hotkey('ctrl','a')
                speak('done')

            elif 'cut' in statement or 'parcel' in statement:
                import pyautogui
                pyautogui.hotkey('ctrl','x')
                speak('done')
            
            elif 'copy' in statement:
                import pyautogui
                pyautogui.hotkey('ctrl','c')
                speak('done')

            elif 'paste' in statement or 'delivery' in statement:
                import pyautogui
                pyautogui.hotkey('ctrl','v')
                speak('done')
            
            elif 'delete tab' in statement  or  'delete the tab' in statement :
                import pyautogui
                pyautogui.hotkey('ctrl','w')
                speak('done')

            elif 'delete' in statement:
                import pyautogui
                pyautogui.press('delete')
                speak('done')

            elif 'refresh' in statement:
                import pyautogui
                pyautogui.hotkey('fn','f5')
                speak('done')

            elif 'open new tab' in statement:
                import pyautogui
                pyautogui.hotkey('ctrl','t')
                speak('done')

            elif 'scroll' in statement:
                import pyautogui
                pyautogui.press('down')
                speak('done')
            
            elif 'open maps'in statement or 'visit maps' in statement or 'launch maps' in statement or 'run maps' in statement:
                speak('opening maps')
                webbrowser.open('https://www.google.com/maps/@17.1567099,80.176346,15z?entry=ttu')
                window.maxsize()
                speak('done')

            elif "open stackoverflow" in statement or 'visit stackoverflow' in statement or 'launch stackoverflow' in statement or 'run stackoverflow' in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")
                window.maxsize()           

            elif 'open google' in statement or 'visit google' in statement or 'launch google' in statement or 'run google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")

            elif 'open gmail' in statement or 'visit gmail' in statement or 'launch gmail' in statement or 'run gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
            elif "open youtube" in statement  or 'visit youtube' in statement or 'launch youtube' in statement or 'run youtube' in statement:
                speak("Opening youtube" ) 
                webbrowser.open("https://youtube.com/")
                window.maxsize()
            elif "play shots" in statement or "play shorts" in statement:
                speak("playing shorts")
                webbrowser.open("https://www.youtube.com/shorts/cFXrj4Kdg7E")
                window.maxsize()
                speak('done')

            elif 'play' in statement:
                speak('sure')
                import pywhatkit
                statement.replace('play','')
                pywhatkit.playonyt(statement)
            
            elif 'open' in statement or 'visit' in statement or 'launch ' in statement or 'run' in statement:
                a=statement.replace('open','')
                speak(f"Sure,Opening {a}")
                import pyautogui as p
                p.press('win')
                sleep(2)
                mes=a
                p.typewrite(mes)
                sleep(2)
                p.press('enter')
                window.maxsize()         

            elif 'battery' in statement:
                import psutil
                battery = psutil.sensors_battery()
                percent = battery.percent
                speak("Battery Percentage:{}".format(percent))
                print("Battery Percentage:{}".format(percent))

            elif 'about my pc' in statement or 'system configurations' in statement :
                import platform
                system = platform.system()
                version = platform.version()
                memory = psutil.virtual_memory()
                total_memory = memory.total
                available_memory = memory.available
                speak("System: {}".format(system))
                speak("version: {}".format(version))
                speak("total_memory: {}".format(total_memory))
                speak("available_memory {}".format(available_memory))


            elif 'who is' in statement or 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement = statement.replace("who is", "")
                statement = statement.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    speak(results)
                    print("Chitti: " + results)
                    #update_labels(statement,results)
                except wikipedia.exceptions.PageError:
                    speak("I'm sorry, I couldn't find any information on that topic.")


            elif any(word in tokens for word in ['date', 'today']):
                import datetime
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                response = f"Today's date is {current_date}."
                speak(response)
                print("Chitti :"+response)
            

            elif "weather" in statement :
                api_key = "8ef61edcf1c576d65d836254e11ea420"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"

                speak("What's the city name?")
                city_name = get_user_input().lower()
                if city_name == "":
                    speak("network error")
                else:
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response = requests.get(complete_url)
                    data = response.json()

                    if data["cod"] != "404":
                        main_data = data["main"]
                        current_temperature_kelvin = main_data["temp"]
                        current_temperature_celsius = current_temperature_kelvin - 273.15
                        current_humidity = main_data["humidity"]
                        weather_data = data["weather"]
                        weather_description = weather_data[0]["description"]

                        speak(f"Temperature in Celsius is {current_temperature_celsius:.2f}")
                        print(f"Temperature in Celsius = {current_temperature_celsius:.2f}")
                        speak(f"Humidity in percentage is {current_humidity:.2f}")
                        print(f"Humidity (in percentage) = {current_humidity:.2f}")

                        speak("Description: " + str(weather_description))
                        print("Description = " + str(weather_description))
                    else:
                        speak("City Not Found")
            

            elif "click my photo" in statement or 'take a photo' in statement or 'take a pick' in statement or 'take a selfie' in statement or 'take a pic' in statement or 'click a selfie' in statement:
                import pyautogui
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("SMILE")
                pyautogui.press("enter")

            elif 'who are you' in statement or 'what can you do' in statement or 'what are you feature' in statement or 'how can you help me' in statement:
                speak('I am Chitti version 2 point o  your persoanl assistant. I am programmed to  help you with minor tasks like'
                    'opening apps and webpages ,predict time,take a photo,predict weather in different cities get top headline news from times of india and i can send messages in whatsapp and telegram and i can do many more things , i was developed by saidharagani')

            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement or "who developed you" in statement:
                speak("I was built by sai")
                print("I was built by sai")

            elif "news" in statement:
                api_dict = {
                    "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b687962ca49e42bea7899f0b2e66c925",
                    "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=b687962ca49e42bea7899f0b2e66c925",
                    "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=b687962ca49e42bea7899f0b2e66c925",
                    "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=b687962ca49e42bea7899f0b2e66c925",
                    "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=b687962ca49e42bea7899f0b2e66c925",
                    "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b687962ca49e42bea7899f0b2e66c925"
                }
                content = None
                url = None
                speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
                field = get_user_input()
                for key, value in api_dict.items():
                    if key.lower() in field.lower():
                        url = value
                        print(url)
                        print("URL was found")
                        break
                    else:
                        url = True
                if url is True:
                    print("URL not found")

                news = requests.get(url).json()
                speak("Here is the first news.")

                counter = 0  # Track the number of news articles read
                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    speak(str(new["title"]))
                    counter += 1

                    if counter == 3:  # After reading 3 news articles
                        speak("Do you want more news?")
                        response = get_user_input().lower()
                        if "yes" in response:
                            speak("Okay, here are some more news articles.")
                        else:
                            speak("Alright, I will stop.")
                            break
    
            
            elif "write a note" in statement:
                import pyautogui
                pyautogui.press('win')
                sleep(2)
                mes='notepad'
                keyboard.write(mes)
                sleep(2)
                keyboard.press('enter')
                sleep(1)
                window.maxsize()
                speak('Speak the text.')
                sai = get_user_input() 
                textt = sai.replace('terminate', '').strip()
                keyboard.write(textt)
                for char in textt:
                    keyboard.write(char)
                    time.sleep(0.1)

                time.sleep(1)
                if "terminate" in sai:
                    try:
                        keyboard.press('ctrl+s')
                        time.sleep(1)  
                        save = os.path.join(os.path.expanduser("~"), "Documents")  
                        timestamp = time.strftime("%Y%m%d%H%M%S")
                        file_name = f"note_{timestamp}.txt"
                        save_path = os.path.join(save, file_name)
                        keyboard.write(save_path)
                        keyboard.press('enter')
                        speak('File saved successfully.')
                        speak("File saved as " + file_name)
                    except Exception as e:
                        print("An error occurred while saving the file:", str(e))
                        speak("Sorry, an error occurred while saving the file.")
                        speak("Please try again.")

            
            elif "search" in statement:
                query = statement.replace('search','').strip()
                url = f"https://www.google.com/search?q={query}"
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                div_element = soup.find('div', class_="BNeawe s3v9rd AP7Wnd") 
                if div_element:
                    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
                    webbrowser.get('chrome').open(url)
                    text = div_element.get_text()
                    speak(text)
                else:
                    speak("im still learning ,can you ask me something else")

            else : 
                speak("im still learning ,can you ask me something else")
def greet():       
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello,Good Morning")
        speak("Hello,Good Morning")
        
    elif hour>=12 and hour<18:
        print("Hello,Good Afternoon")
        speak("Hello,Good Afternoon")
        
    else:
        print("Hello,Good Evening")
        speak("Hello,Good Evening")
greet()
run_voice_assistant()