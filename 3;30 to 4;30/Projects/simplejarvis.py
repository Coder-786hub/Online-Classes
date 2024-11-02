


import pyttsx3
import speech_recognition
import datetime
import time
import pyautogui
import random
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    """Function to make the assistant speak."""
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Takes voice input from the user and returns the query."""
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "none"
    return query

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you?")
    
    while True:
        query = takeCommand().lower()

        if "hello" in query:
            speak("Hello Sir, How are you?")
        
        elif "how are you" in query:
            speak("I'm doing great, sir!")
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")
        
        elif "screenshot" in query:
            im = pyautogui.screenshot()
            filename = str(random.randint(1, 100)) + ".jpg"  # Generate random number and create the filename
            im.save(filename) 
            speak("Screenshot taken, sir.")
        
        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            time.sleep(2)
            speak("Smile!")
            pyautogui.press("enter")
        
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        
        elif "news" in query:
            webbrowser.open("https://news.google.com")
            speak("Here are the latest headlines.")
        
        elif "tired" in query:
            speak("Playing your favorite songs.")
            song_urls = [
                "https://www.youtube.com/watch?v=VHgocXq76cM",
                "https://www.youtube.com/watch?v=XwmsxKJpCw4",
                "https://www.youtube.com/watch?v=PKIlSv9yMTY"
            ]
            random_song = random.choice(song_urls)
            webbrowser.open(random_song)
        
        elif "shutdown system" in query:
            speak("Shutting down the system.")
            # You can use os.system("shutdown /s /t 1") for Windows shutdown
        
        elif "exit" in query or "take rest" in query:
            speak("Goodbye, sir. Have a great day!")
            break
