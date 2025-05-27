import speech_recognition as sr
import pyttsx3
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

if __name__ == "__main__":
    speak("How can I assist you?")
    command = take_command()
    print("Command:", command)

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "hello" in command:
        speak("Hello! I'm your assistant.")
#pip install transformers accelerate
