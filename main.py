
import requests
import json
import pyttsx3
city=input("Enter the name of a city:")
url=f"https://api.weatherapi.com/v1/current.json?key=e1e2c5a66a47414ebf5123740232612&q={city}"

r=requests.get(url)

wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
engine = pyttsx3.init()
speak=f"Temperature of {city} is{w}"
engine.say(speak)
engine.runAndWait()