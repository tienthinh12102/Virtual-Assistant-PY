import speech_recognition
import wikipedia
from gtts import gTTS
from datetime import date
from datetime import datetime
import os

wikipedia.set_lang("vi")
robot_ear = speech_recognition.Recognizer()
robot_brain = "Tôi đang nghe bạn đây"
#Nghe
with speech_recognition.Microphone() as mic:
	print("Robot: " + robot_brain)

	audio =robot_ear.record(mic, duration=3) 

try:
	you = robot_ear.recognize_google(audio,language='vi-VN')
	print("You: " + you)
except:
	you == "Tôi không hiểu bạn nói gì ?"
	print("Robot: "+ you)

#Bộ não AI
if you == "":
	robot_brain = "Tôi không nghe thấy bạn, hãy thử lại"
elif "chào" in you:
	robot_brain = "Xin chào Thịnh sama"
elif "hôm nay" in you:
	today = date.today()
	robot_brain = today.strftime("%B %d, %Y")
elif "ngày" in you:
	day = date.today()
	robot_brain = day.strftime("Hôm nay ngày "+"%d")
elif "giờ" in you:
	now = datetime.now()
	robot_brain = now.strftime("%H gio %M phút %S giây")
elif "rap" in you:
	robot_brain = ("Big city boi big city boy")
elif "tôi" in you:
	robot_brain = ("Thịnh good boi đẹp trai thanh lịch cấp vũ trụ")
elif "tổng thống" in you:
	test = you
	robot_brain = wikipedia.summary("Tổng thống mỹ hiện tại", sentences = 1)
elif "hát" in you:
	robot_brain = ("đưa tay đây nào, mãi bên nhau bạn nhớ, You make me feel like, I got everything")
else:
	cauhoi = you 
	robot_brain = wikipedia.summary(cauhoi, sentences = 1)

print("Robot: " + robot_brain)

#Nói
tts = gTTS(text = robot_brain,lang='vi')
tts.save("pcvoice.mp3")
os.system("start pcvoice.mp3")