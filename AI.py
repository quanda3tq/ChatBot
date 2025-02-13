import speech_recognition
import pyttsx3
import wikipedia
from datetime import date, datetime

# Khởi tạo giọng nói
Robot_mouth = pyttsx3.init()
voices = Robot_mouth.getProperty('voices') 
Robot_mouth.setProperty('voice', voices[1].id)  # Chọn giọng nữ (1), giọng nam là (0)
Robot_mouth.setProperty('rate', 200)

# Khởi tạo nhận diện giọng nói
Robot_ear = speech_recognition.Recognizer()
Robot_brain = ""

# Chọn phương thức nhập một lần duy nhất
while True:
    print("\nChoose input method: (1) Voice, (2) Keyboard")
    choice = input("Enter 1 or 2: ").strip()

    if choice in ["1", "2"]:
        break  # Thoát khỏi vòng lặp khi chọn đúng
    else:
        print("Invalid choice! Please enter 1 or 2.")

while True:
    if choice == "1":
        # Nhận dữ liệu từ microphone
        with speech_recognition.Microphone(device_index=None) as mic:  
            print("Robot: I'm listening...")
            audio = Robot_ear.listen(mic)

        print("Robot: ...")

        try:
            you = Robot_ear.recognize_google(audio)
        except:
            you = ""
    else:
        # Nhập từ bàn phím
        you = input("You: ").strip()

    print("You: " + you)

    # Xử lý câu lệnh
    your_lower = you.lower()
    
    if "hello" in your_lower:
        Robot_brain = "Hello DFox"
    elif "today" in your_lower: #Ngày
        today = date.today()
        Robot_brain = today.strftime("%B %d, %Y")
    elif "time" in your_lower:  #Giờ
        now = datetime.now()
        Robot_brain = now.strftime("%H hours %M minutes")
    elif "who am i" in your_lower:  # =)
        Robot_brain = "Maybe you are my boss, a good person"
    elif "introduce yourself" in your_lower:    #Giới thiệu về bản thân chatbot
        Robot_brain = "I'm a Chatbot made by DF"
    elif "thank" in your_lower: #Cảm ơn
        Robot_brain = "You're welcome. Do you have any questions?"
    elif "search" in your_lower or "who is" in your_lower:
        try:
            query = your_lower.replace("search", "").replace("who is", "").strip()
            if query:
                Robot_brain = wikipedia.summary(query, sentences=2)  # Lấy 2 câu đầu tiên từ Wikipedia
            else:
                Robot_brain = "Please provide a topic to search on Wikipedia."
        except wikipedia.exceptions.DisambiguationError:
            Robot_brain = "There are multiple results. Please be more specific."
        except wikipedia.exceptions.PageError:
            Robot_brain = "I couldn't find anything on Wikipedia about that."
    elif "bye" in your_lower or "stop" in your_lower or "no" in your_lower:       #Dừng chương chình
            Robot_brain = "See you again"
            print("Robot: " + Robot_brain)
            Robot_mouth.say(Robot_brain)
            Robot_mouth.runAndWait()
            break  # Thoát chương trình

    else:
        Robot_brain = "I don't understand. Please say again."

    print("Robot: " + Robot_brain)

    # Nói
    Robot_mouth.say(Robot_brain)
    Robot_mouth.runAndWait()
