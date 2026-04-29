import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time

# Initialize TTS engine once
engine = pyttsx3.init()
engine.setProperty('rate', 170)   # speaking speed
engine.setProperty('volume', 1.0) # volume (0.0 to 1.0)

def speak(text):
    """Make the bot speak with stability fixes"""
    print("Bot:", text)  # also print what bot says
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.3)  # small pause to prevent cutoff

# Listen to microphone
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # handle background noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service is down, please check your internet.")
        return ""

# Main Voice Bot
def voice_bot():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "mail" in command or "gmail" in command:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif "hello" in command:
            speak("Hello! How are you today?")

        elif "who are you" in command:
            speak("I am your simple Python voice assistant.")

        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            if command != "":
                speak("I can answer simple questions or open apps like YouTube, Google, or Gmail.")


# Run Bot
if __name__ == "__main__":
    voice_bot()