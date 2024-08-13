import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis Sir. I am here to help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
# it converts the audio input into string

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() # 

        #logic for executing tasks based on query
        if "how are you" in query:
            speak("I'm fine sir, how can i help you ?")

        elif "who are you" in query:
            speak("Sir I am Jarvis personal assistant ")

        elif "who is aditi" in query:
            speak("Aditi is a good girl. And Aditi is also known as Bhootu ")    

        elif "count a b c d" in query:
            speak("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ")

        elif "count 1 to 20" in query:
            speak("1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 ")    

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...please wait')
            query = query.replace("wikipedia", "")
            results =  wikipedia.summary(query, sentences = 2)
            speak("wikipedia says")
            print(results)
            speak(results)

        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open cartoon' in query:
            webbrowser.open("https://www.youtube.com//watch?v=xG4QTYMdQIw")    

        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')

        elif 'open mail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')    

        elif 'open icloud' in query:
            webbrowser.open('https://gu.icloudems.com/corecampus/index.php')    

        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')

        elif 'play music'in query:
            music_dir = "D:\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play lakdi ki kathi'in query:
            music_dir = "D:\lakdi ki kathi"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play johny johny yes papa'in query:
            music_dir = "D:\jony jony yes papa"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))        

        elif 'play music'in query:
            music_dir = "D:\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\kumar\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)  

        elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks you for using Jarvis Sir")
            exit()            

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{9534292997}", message)              