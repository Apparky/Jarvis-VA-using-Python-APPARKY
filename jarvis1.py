import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import json
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        print("Welcome!\nApparky wishes you \n Good Morning!")
        speak("Welcome!\nApparky wishes you \n Good Morning!")

    elif 12 <= hour < 18:
        print("Welcome!\nApparky wishes you \n Good Afternoon!")
        speak("Welcome!\nApparky wishes you \n Good Afternoon!")

    elif 18 <= hour < 21:
        print("Welcome!\nApparky wishes you \n Good Evening!")
        speak("Welcome!\nApparky wishes you \n Good Evening!")

    else:
        print("Welcome!\nApparky wishes you \n Good Night!")
        speak("Welcome!\nApparky wishes you \n Good Night!")


speak(
    "Hello ! I am jarvis\n Apparky Voice Assistant \nYou are the only one who created me \n I am greatful to you that you gave me the life\n Thank you sir for creating me")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("say that again please......")
        speak("say that again sir.....")
        return "None"
    return query


if __name__ == '__main__':
    #
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia.....")
            print(results)
            speak(results)
        elif 'what is the news of india' in query:
            speak("News for today")
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=3196e5c94880464fbb4f815b17d7c345"
            news = requests.get(url).text
            news = json.loads(news)

            print(news["articles"])
            arts = news['articles']
            for article in arts:
                speak(article['title'])
                speak("moving on to the next news... Listen carefully")

        elif 'are you a robot' in query:
            speak(
                "yes sir! i am a robot with lots of useful information regarding you and your computer\n i also have information regarding your Team member too..")
        elif 'who are you' in query:
            speak("My name is jarvis and\n I am your personal assistant ")
        elif 'get Lost' in query:
            speak("sorry sir! have i done anything wrong sir!\n i am really very sorry for my mistakes")
        elif ' love me' in query:
            speak("yes sir!i love you very much sir\n you are the only one who created me")
        elif 'do you know my name' in query:
            speak("yes sir! your name is Apparky")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("yes sir!!opening you tube for you sir!")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("yes sir!! opening google for you sir!!")
        elif 'close google' in query:
            webbrowser.close()
            speak("yes sir!! closing google for you sir!!")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("searching the music for you sir!!")
            music_dir = 'C:\\'
            songs = random.choice(os.listdir(music_dir))
            print(random.choice(songs))
            os.startfile(os.path.join(music_dir, songs))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Avi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        else:
            speak('Command is not recognised...!')

    # music_dir("songs","stop")
    takeCommand()
