import os, webbrowser, sys, requests, subprocess, pyttsx4

engine = pyttsx4.init()
voices = engine.getProperty('voices')
desired_voice = voices[0]
engine.setProperty('voice', desired_voice.id)
engine.setProperty('rate', 180)

def speaker(text):
    engine.say(text)
    engine.runAndWait()
    
   
def weather():
    params = {'q': 'Bonn', 'units': 'metric', 'lang': 'ru', 'appid': '4f62995cdbe1859c14b53952ff2cd95b'}
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
    w = response.json()
    speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

def youtube():
    webbrowser.open('https://www.youtube.com/', new=2)

def spotify():
    subprocess.Popen("C:/Users/OG/AppData/Local/Programs/youtube-music-desktop-app/YouTube Music Desktop App.exe")


def offBot():
    sys.exit()

def offpc():
    os.system('shutdown/s')


def passive():
    pass