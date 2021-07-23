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
		R.pause_threshold = 1.5
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
		talk("Меня зовут Anna")
	elif task in "как дела как делишки как настроение":
		talk(random.choice(data.howareyouanswer))
	elif task == "курс доллара":
		USD_UAH = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0&aqs=chrome.1.69i57j0i20i263i433j0i433j0i20i263i433j0j0i131i433j0j0i10l2j0.2318j0j7&sourceid=chrome&ie=UTF-8'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
		full_page = requests.get(USD_UAH, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
		talk("Курс доллара " + str(convert[0].text) + " гривны")
	elif task == "курс евро":
		EURO_UAH = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&sxsrf=ALeKk01HgiwJ4968DbtGKjBwcTxZRtqyeg%3A1627066794718&ei=qhH7YICyK-XhrgSGh5PgBg&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgcIABBHELADOgcIABCwAxBDOgcIIxDqAhAnOgQIIxAnOgsILhCxAxDHARCjAjoICC4QxwEQrwE6BAgAEEM6BwgAELEDEEM6DQgAEIcCELEDEIMBEBQ6BwgjELECECc6BwgAEIcCEBQ6BwgAEMkDEENKBAhBGABQoaoGWOHLBmC6zgZoA3ACeACAAZEBiAH4DJIBBDMuMTKYAQCgAQGqAQdnd3Mtd2l6sAEKyAEKwAEB&sclient=gws-wiz&ved=0ahUKEwiAr8yS8PnxAhXlsIsKHYbDBGwQ4dUDCA8&uact=5'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
		full_page = requests.get(EURO_UAH, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
		talk("Курс евро " + str(convert[0].text) + " гривны")
	elif task == "курс биткоина":
		BTC_USD = 'https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sxsrf=ALeKk01BVM2xWAtCHEYUoeygNiQdCfCeEg%3A1627066904451&ei=GBL7YP7fGq_rrgSFra7oDA&oq=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%BA+%D0%B4%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgjECc6BwgAEIcCEBQ6CAgAELEDEIMBOgQIABBDOg0IABCHAhCxAxCDARAUOgcIABCxAxBDOgoIABCHAhCxAxAUSgQIQRgAUIDDCliC1gpgmd0KaABwAngAgAHcAYgBhgySAQYxLjExLjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
		full_page = requests.get(BTC_USD, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
		talk("Курс биткоина " + str(convert[0].text) + " доллара")
	elif task == "открой браузер":
		talk("Открываю...")
		webbrowser.open_new("https://google.com")
	elif task == "спасибо":
		talk("Рада стараться!")
	elif task == "молодец":
		talk("Спасибо!")
	elif task == "открой youtube":
		talk("Открываю...")
		webbrowser.open_new("https://www.youtube.com/")
	elif task == "открой гитхаб":
		talk("Открываю...")
		webbrowser.open_new("https://github.com/")
	elif task in data.flip:
		flip_coin = ["Орел", "Решка"]
		talk(random.choice(flip_coin))

while True:
	make(command())