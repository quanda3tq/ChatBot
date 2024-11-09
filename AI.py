import speech_recognition
import pyttsx3
from datetime import date, datetime

Robot_mouth = pyttsx3.init()
voices = Robot_mouth.getProperty('voices') 
Robot_mouth.setProperty('voice', voices[2].id)   #Changes voices. 1 for female, 0 for male
Robot_mouth.setProperty('rate', 200)

Robot_ear = speech_recognition.Recognizer() 
Robot_brain = ""

while True:
    #Nghe
    with speech_recognition.Microphone(device_index=4) as mic:
        print("Robot: I'm listening")
        audio = Robot_ear.listen(mic)
        
    print("Robot: ...")

    try:
        you = Robot_ear.recognize_google(audio)
    except:
        you = ""
    print("you: " + you)
    
    #Hieu
    if "hello" in you:
        Robot_brain = "Hello DFox"
    elif "today" in you:
        today = date.today()
        Robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        Robot_brain = now.strftime("%H hourse %M")
    elif "bye" in you:
        Robot_brain = "See you again"
        #Noi
        Robot_mouth.say(Robot_brain)
        Robot_mouth.runAndWait()
        print("Robot: " + Robot_brain)
        break
    elif "who am I" in you:
        Robot_brain = "maybe you are my boss, a good boy"
    elif "introduce yourself" in you:
        Robot_brain = "I'm a Chatbot make by DF"
    elif "thank" in you:
        Robot_brain = "you're welcom"
    else:
        Robot_brain = "again"

    print("Robot: " + Robot_brain)
#Noi
    Robot_mouth.say(Robot_brain)
    Robot_mouth.runAndWait()