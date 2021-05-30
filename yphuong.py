import speech_recognition
import wikipedia
from gtts import gTTS
from datetime import date
from datetime import datetime
import os

robot_ear = speech_recognition.Recognizer()
def speak(robot_brain):
	tts = gTTS(text = robot_brain,lang='vi')
	tts.save("pcvoice.mp3")
	os.system("start pcvoice.mp3")
#Nghe
while True:
	pass
	with speech_recognition.Microphone() as mic:
		print("Em iu đang nghe ...")
		audio = robot_ear.record(mic, duration=5) 
	try:
		you = robot_ear.recognize_google(audio,language='vi-VN')
		print("You: " + you)
	except:
		you == "Tôi không hiểu bạn nói gì ?"
		print("Em iu: "+ you)

		#Bộ não AI
	if you == "":
		robot_brain = "Tôi không nghe thấy bạn, hãy thử lại"
	elif "Xin chào" in you:
		robot_brain = "Xin chào Thịnh sama"
		speak(robot_brain)
	elif "Hello" in you:
		robot_brain = "Xin chào anh yêu <3"
		speak(robot_brain)
	elif "Chào" in you:
		robot_brain = "Xin chào Thịnh sama"
		speak(robot_brain)
	elif "hôm nay" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
		speak(robot_brain)
	elif "ngày" in you:
		day = date.today()
		robot_brain = day.strftime("Hôm nay là ngày %d")
		speak(robot_brain)
	elif "giờ" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H gio %M phút %S giây")
		speak(robot_brain)
	elif "rap" in you:
		robot_brain = ("Big city boi big city boy")
		speak(robot_brain)
	elif "tôi" in you:
		robot_brain = ("Thịnh good boi đẹp trai thanh lịch cấp vũ trụ")
		speak(robot_brain)
	elif "Thành Đạt" in you:
		robot_brain = ("là thằng Đạt ngu hay uống nước cam và thích chơi đồ")
		speak(robot_brain)
	elif "Thành đạt" in you:
		robot_brain = ("là thằng Đạt ngu hay uống nước cam và thích chơi đồ")
		speak(robot_brain)
	elif "thành đạt" in you:
		robot_brain = ("là thằng Đạt ngu hay uống nước cam và thích chơi đồ")
		speak(robot_brain)
	# elif you:
	# 	wikipedia.set_lang("vi")
	# 	robot_brain = wikipedia.summary(you, sentences = 1)
	# 	speak(robot_brain)
	elif "hát" in you:
		robot_brain = ("đưa tay đây nào, mãi bên nhau bạn nhớ, You make me feel like, I got everything")
		speak(robot_brain)
	else:
		robot_brain = ("Tôi không hiểu")
		speak(robot_brain)
	print("Robot: " + robot_brain)

#Nói
