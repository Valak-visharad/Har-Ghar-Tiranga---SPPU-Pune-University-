# from _typeshed import WriteableBuffer
from email import message
from pyaudio import paNoDevice
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import pywhatkit as pwk
import pyjokes as pj
import requests
import smtplib 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am REX, how can i help you today")


def takeCommand():
    # It takes microphone in put from the  user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        # r.adjust_for_ambient_noise(source,duration = 3)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

def get_weather(city):
            result = requests.get(url.format(city,'99c9db04fb83ce087fb75dedc820a6ae'))
            if result:
                json = result.json() 
                city = json['name']
                country = json['sys']['country']
                temp_kelvin = json['main']['temp']
                temp_celsius = temp_kelvin - 273.15
                temp_farenheit = (temp_celsius) * 9/5 +32
                weather = json['weather'][0]['main']
                a=str(temp_celsius)
                temp_celsius=a[0:4]
                final = (city,country,temp_celsius,temp_farenheit,weather)
                print(final)
                if weather=='rainy':
                    speak(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ,please carry an umbrella with u while going out ")
                    print(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ,please carry an umbrella with u while going out") 
                elif weather=='stormy':
                    speak(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ,please stay at home for today")
                    print(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ,please stay at home for today") 
                else:
                    speak(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree   ,have a nice day ")
                    print(f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree   , have a nice day ") 

            else:
                return None

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nilayv123@gmail.com', 'your-password')
    server.sendmail('nilayv123@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube ..")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'screenshot' in query: 
            im1 = pyautogui.screenshot()
            im1.save('my_screenshot.png')
            # im2 = pyautogui.screenshot('my_screenshot2.png')
            speak("Screenshot has been taken and saved sucessfully..")

        elif "youtube" in query:
            speak("Which song do you want me to play on youtube")
            song_input = takeCommand()
            pwk.playonyt(song_input)

        elif 'whatsapp message' in query:
            speak("Please say the number to whom i should send the whatsapp message")
            phoneNo = takeCommand()
            countryCode = "+91" + phoneNo
            print(countryCode)
            speak("Please say what message you whant to send")
            message = takeCommand()
            speak("Please say the hour when to send whatsapp Message according to 24 hours format")
            hours = takeCommand()
            if 'tu' in hours:
                hours = hours.replace("tu","2")
                
            int_hours = int(hours)
            print(int_hours)
            speak("Please say the minutes when to send whatsapp Message according to 24 hours format")
            minutes = takeCommand()
            int_minutes = int(minutes)

            pwk.sendwhatmsg(countryCode, message, int_hours,int_minutes)

        
        elif 'remainder' in query:
            pass


        elif 'timer' in query:
            pass
           

        elif 'weather' in query:
            
            if "tell me about today's weather in" in query:
                query = query.replace("tell me about today's weather in ","")
                city = query 
            
            elif "what is today's weather" in query:
                speak("Which city do you want to know the weather of")
                city = takeCommand()

            
            get_weather(city)
    

        elif 'joke' in query:
            joke = pj.get_joke()
            print(joke)
            speak(joke)

        elif 'remember' in query:
            remember = takeCommand()
            with open ("remember.txt",'a') as f:
                rem = f.write(remember)
            speak("Is this all you want me to remember")
            ans = takeCommand()

        elif 'to remember' in query:
            old = takeCommand()    
            with open ("remember.txt",'r') as olffile:
                oldf = f.read(remember)
            speak (oldf)
        
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                # speak("Sorry my friend harry bhai. I am not able to send this email")

        
