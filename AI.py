import speech_recognition
import pyttsx3
import wikipedia
from datetime import date, datetime

Robot_mouth = pyttsx3.init()
voices = Robot_mouth.getProperty('voices') 
Robot_mouth.setProperty('voice', voices[1].id)   #Changes voices. 1 for female, 0 for male
Robot_mouth.setProperty('rate', 200)

Robot_ear = speech_recognition.Recognizer() 
Robot_brain = ""

while True:
    #Nghe
    with speech_recognition.Microphone(device_index=None) as mic: #4: Mic loa ngoai laptop 
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
    elif "introduce yourself" in you:
        Robot_brain = "I'm a Chatbot make by DF"
    elif "thank" in you:
        Robot_brain = "you're welcom"

    elif "search" in you or "who is" in you or "What about" in you: #Wikipedia
        try:
            query = you.replace("search", "").replace("who is", "").strip()
            Robot_brain = wikipedia.summary(query, sentences=2)  # Lấy 2 câu đầu tiên từ Wikipedia
        except wikipedia.exceptions.DisambiguationError as e:
            Robot_brain = "There are multiple results. Please be more specific."
        except wikipedia.exceptions.PageError:
            Robot_brain = "I couldn't find anything on Wikipedia about that."
    
    elif "bye" in you: #Goobye, Dừng chatbot
        Robot_brain = "See you again"
        #Noi
        Robot_mouth.say(Robot_brain)
        Robot_mouth.runAndWait()
        print("Robot: " + Robot_brain)
        break
    else:
        Robot_brain = "I don't understand. Please say again."

    print("Robot: " + Robot_brain)
#Noi
    Robot_mouth.say(Robot_brain)
    Robot_mouth.runAndWait()