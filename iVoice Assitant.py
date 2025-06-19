import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    
    for voice in voices:
        if "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("I'm having trouble connecting. Please check your internet.")
        return ""

def respond(command):
    if "how r u" in command or "how are you?" in command:
        speak("I am fine. What about you?")
    elif "hello" in command:
        speak("hello sir!! how you are doing?")
    elif "your name" in command:
        speak("My name is Isabella. I am your personal voice assistant.")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "open youtube" in command:
        speak("Opening YouTube") 
        webbrowser.open("https://www.youtube.com") 
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "tell me a joke" in command or "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "exit" in command or "stop" in command:
        speak("Goodbye, have a great day!")
        exit()
    else:
        speak("Sorry, I didn't understand that. Can you say it again?")

if __name__ == "__main__":
    speak("Hello, I am Isabella. How can I assist you?")
    while True:
        user_command = listen()
        if user_command:
            respond(user_command)
