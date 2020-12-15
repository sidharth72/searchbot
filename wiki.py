import wikipedia as wk
import speech_recognition as sr
from gtts import gTTS
import os

def Search():
	mic = sr.Recognizer()

	with sr.Microphone() as source:
		print("speak now:")
		
		audio = mic.listen(source)
		mic.adjust_for_ambient_noise(source)

		try:
			text = mic.recognize_google(audio)
			print(text)
			wiki_summmary = wk.summary(text)
			print(wiki_summmary)

			language = "en"

			output = gTTS(text = wiki_summmary,lang = language)

			output.save("summary.mp3")

			os.system("start summary.mp3")

		except:

			print("Didnt get that")

Search()