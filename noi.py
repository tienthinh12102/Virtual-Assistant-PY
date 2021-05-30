import pyttsx3
import wikipedia
import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Robot: I'm Listening")
	audio =robot_ear.record(mic, duration=3) 
try:
	you = robot_ear.recognize_google(audio,language='vi-VN')
except:
	you == "..."

print("You: " + you)

if you == "":
	robot_brain = "Tôi không nghe thấy bạn, hãy thử lại"
elif "chào" in you:
	robot_brain = "Donald Trump"

engine = pyttsx3.init()
engine.say(wikipedia.summary(robot_brain, sentences = 1))
engine.runAndWait()