import pyttsx3
import datetime
from time import sleep
import speech_recognition as sr
import wikipedia
import os
import random
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate' , 180)
engine.setProperty('voice' , voices[1].id)
  




def speak(audio):
	engine.say(audio)
	engine.runAndWait()
	engine.stop()

def wishme():
	
	hour = int(datetime.datetime.now().hour)

	if hour>=0 and hour<12:
		speak('Good Morning Sir')
		#speak('How May I help you ')

	elif hour>=12 and hour<=17:
		speak("Good Afternoon Sir....")
		#speak('How May I help you  ')

	elif hour>=18 and hour<=20:
		speak('Good Evening Sir')
		#speak('How May I help you ')

	
	else:
		speak("Good Night Sir......Please go and sleep It's No time for work")


def voiceInput():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		r.pause_threshold = 1
		r.energy_threshold = 500
		audio = r.listen(source)
	
	try:
		print('Recognizing...')
		query = r.recognize_google(audio, language="en-in")
		print(f"Boss: {query}\n")

	except Exception as e:
		print(e)
		print("Say that again please")
		return "None"
	
	return query



wishme()
rand = random.randrange(53)
chromePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
edgePath=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
youtubeUrl="www.youtube.com"
googleUrl= "www.google.com"

while 1:

	q = voiceInput().lower()

	while('friday' not in q):
		q = voiceInput().lower()


	if 'are you there' in q or 'are you up'in q :
		speak('Always at your service boss')
		sleep(0.3)
		speak('What can I do for you sir')


	elif 'you up' in q:
		speak('For you sir always')
		sleep(0.1)
		speak('What you want me to do')

	elif 'hello friday' in q or 'hi friday' in q or 'hey friday' in q or 'hey j' in q :
		wishme()


	elif 'friday' in q:
		speak("Yaa that's me ")
		sleep(0.2)
		speak('What i have to do sir')



	q1 = voiceInput().lower()
	if 'do you know me' in q1:
		speak('You are my boss.. I will do anything that you want sir')

	elif 'who are you' in q1:
		speak('I am friday a personal assistant of mr. naman agarwal')
		sleep(0.5)
		speak('he is my boss  I will do anything that he wants')

	elif 'i am in love' in q1:
		speak('yes i know that sir')

	elif ('play' in q1 and 'music' in q1) or ('listen' in q1 and 'music' in q1):
		speak('Playing your favourites  Sir')
		music_dir  = "S:\\Musics"
		songs = os.listdir(music_dir)
		os.startfile(os.path.join(music_dir , songs[rand]))

	elif 'open vs code' in q1 or 'open code' in q1:
		speak('opening visual studio code')
		code_path=r"C:\\Users\\HP\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
		os.startfile(code_path)

	elif 'open web browser' in q1 or 'open browser' in q1:
		speak('sir which web browser you want to start')
		sleep(0.2)
		speak('there are two options available')
		sleep(0.2)
		speak('Google Chrome and edge')
		q1= voiceInput().lower()
		if 'open google chrome' in q1 or 'open chrome' in q1 or 'google chrome' in q1:
			speak('Opening google chrome')
			os.startfile(chromePath)
		elif 'open microsoft edge' in q1 or 'open edge' in q1 or 'edge' in q1:
			speak('Opening Edge')
			os.startfile(edgePath)
	
	elif 'open google chrome' in q1 or 'open chrome' in q1:
		speak('Opening google chrome')
		os.startfile(chromePath)

	elif 'open microsoft edge' in q1 or 'open edge' in q1:
		speak('Opening Edge')
		os.startfile(edgePath)

	elif 'open youtube' in q1:
		webbrowser.get(edgePath).open(youtubeUrl)

	elif 'open google' in q1:
		webbrowser.get(chromePath).open(googleUrl)
		

	else:
		speak("I am afraid i can't do that at the moment")


