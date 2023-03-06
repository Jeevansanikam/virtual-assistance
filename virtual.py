import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import psutil
import geocoder
import json
import re
from bs4 import BeautifulSoup
import cv2
import pyzbar.pyzbar as pyzbar
import pyzbar
import numpy as np
import os

listener= aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction

    try:

        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction= listener.recognize_google(speech)
            instruction= instruction.lower()
            if "alexa" in instruction:
                 instruction = instruction.replace('alexa','')
                 print(instruction)

    except:
        pass
    return instruction




def play_alexa():

    instruction = input_instruction()
    print(instruction)
    if"play" in instruction:
        song= instruction.replace('play',"")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif  'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M$p')
        talk('current time ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date"+ date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you')

    elif 'what is your name' in instruction:
        talk('I am alexa, What can i do for you?')

    elif 'battery' in instruction:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        if plugged:
            status = "charging"
        else:
            status = "discharging"
        talk("The battery is currently " + status + " at " + percent + " percent")
        

    elif 'Who is' in instruction:
        human = instruction.replace('Who is', " ")
        info = wikipedia.summary(human, 1)
        talk("searching"+info)
   
    

    elif 'location' in instruction:
        g = geocoder.ip('me')
        location = g.city
        talk("You are currently in " + location)

    elif 'what is(word)' in instruction:
        word = word.lower()
        url = "https://www.dictionary.com/browse/" + word
        html_file = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_file, 'html.parser')
        definition = soup.find_all('div', {'value': '1'})[0].get_text()
        speak("The definition of " + word + " is " + definition)

    




    else:
        talk('Please repeat')

play_alexa()