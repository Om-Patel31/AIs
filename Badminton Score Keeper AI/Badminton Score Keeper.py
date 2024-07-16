import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 250)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand the audio.")
        return "None"
    except sr.RequestError as e:
        speak(f"Error: {e}")
        return "None"

def run():
    while True:
        no_of_matches()

def addpoints(p1, p1points, p2, p2points):
    while True:
        try:
            speak("Which player to add points to?")
            query = takecommand().lower()

            # Sanitize input
            if "points" in query or "add" in query:
                if p1.lower() in query:
                    p1points += 1
                elif p2.lower() in query:
                    p2points += 1
                else:
                    speak("Invalid player name. Please try again.")
                    continue
                speak(f"{p1} has {p1points}. {p2} has {p2points}.")

                # Check for win condition
                if (p1points >= 20 or p2points >= 20) and abs(p1points - p2points) >= 2:
                    if p1points > p2points:
                        speak(f"{p1} has won!")
                    else:
                        speak(f"{p2} has won!")
                    break

            else:
                speak("I didn't catch that. Please say 'add points'.")
                continue

        except ValueError:
            speak("Please provide a valid input.")
            continue
        except Exception as e:
            speak(f"Error occurred: {e}. Please try again.")
            continue

def match():
    engine.say("Enter name of player 1:")
    engine.runAndWait()
    p1 = input("Enter name of player 1:")
    engine.say("Enter name of player 2:")
    engine.runAndWait()
    p2 = input("Enter name of player 2:")
    addpoints(p1, 0, p2, 0)

def no_of_matches():
    start = int(input("Enter the number of matches you want me to score keep: "))
    if start >= 1 and start <= 3:
        for _ in range(start):
            match()
    else:
        speak("Invalid input. Please enter a number between 1 and 3.")

run()