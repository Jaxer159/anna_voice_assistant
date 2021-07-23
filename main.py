import speech_recognition as sr 
import os
import pyttsx3 as px
import sys
import webbrowser
import data
import datetime
import random
import requests
from bs4 import BeautifulSoup

def command():
	R = sr.Recognizer()

	with sr.Microphone() as source:
		print("Говорите...")
		R.pause_threshold = 1
		R.adjust_for_ambient_noise(source, duration=0.5)
		audio = R.listen(source)

	try:
		task = R.recognize_google(audio, language='ru-RU').lower()
		print("[LOG] " + task)
	except sr.UnknownValueError:
		print("[LOG] ValueError")
		task = command()

	return task

def talk(words):
	engine = px.init()
	engine.say(words)
	engine.runAndWait()

def make(task):
	if task in data.hello:
		talk(random.choice(data.hello))
	elif task in data.goodbye:
		talk(random.choice(data.goodbye))
		sys.exit()
	elif task in data.myname:
		talk("Моё имя Anna")
	elif task == "курс доллара к гривне":
		DOLLAR_UAH = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0&aqs=chrome.1.69i57j0i20i263i433j0i433j0i20i263i433j0j0i131i433j0j0i10l2j0.2318j0j7&sourceid=chrome&ie=UTF-8'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
		full_page = requests.get(DOLLAR_UAH, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
		talk("Курс доллара " + str(convert[0].text) + " гривны")

while True:
	make(command())