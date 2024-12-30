import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    """Process the voice command and perform actions."""
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        link = music_library.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}.")
        else:
            speak(f"Sorry, I couldn't find the song {song} in your library.")
    else:
        speak("I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    recognizer = sr.Recognizer()

    while True:
        try:
            # Listen for the wake word
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes, I'm listening.")
                    # Listen for the actual command
                    with sr.Microphone() as source:
                        print("Listening for your command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        process_command(command)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
