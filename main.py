import speech_recognition as sr 
import os
import pyttsx3 as px
import sys
import webbrowser
import data
import datetime
import random

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

while True:
	make(command())