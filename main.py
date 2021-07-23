import speech_recognition as sr 
import os
import pyttsx3 as px
import sys
import webbrowser
import data

def command():
	R = sr.Recognizer()

	with sr.Microphone() as source:
		print("Говорите...")
		R.pause_threshold = 1
		R.adjust_for_ambient_noise(source, duration=1)
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
		talk("Здраствуйте!")

while True:
	make(command())