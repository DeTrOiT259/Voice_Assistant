import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		try:
			print("recognizing...")
			data = recognizer.recognize_google(audio)
			return data
		except sr.UnknownValueError:
			print("Not Understand")


def speechtx(x):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice',voices[0].id )
	rate = engine.getProperty('rate')
	engine.setProperty('rate',150)
	engine.say(x)
	engine.runAndWait()


if __name__ == "__main__":
    if "hey peter" in sptext().lower():
        while True:
            data1 = sptext().lower()
            
            if "your name" in data1:
                name = "my name is peter"
                speechtx(name)
            elif "old are you" in data1:
                age = "i am 1 years old"
                speechtx(age)
            elif 'time' in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(current_time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'joke' in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)
            elif 'play song' in data1:
                add = "C:\songs"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))
            elif 'exit' in data1:
                speechtx("thank you")
                break
            time.sleep(5)
    else:
        print("thanks")


		