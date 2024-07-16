import tkinter as tk
import speech_recognition as sr
import pyttsx3

class TeamScoreTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Team Score Tracker")

        self.teama_label = tk.Label(root, text="Enter the name of team 1:")
        self.teama_label.pack()
        self.teama_entry = tk.Entry(root)
        self.teama_entry.pack()

        self.teamb_label = tk.Label(root, text="Enter the name of team 2:")
        self.teamb_label.pack()
        self.teamb_entry = tk.Entry(root)
        self.teamb_entry.pack()

        self.teama_button = tk.Button(root, text="Add to Team 1", command=self.add_to_team1)
        self.teama_button.pack()

        self.teamb_button = tk.Button(root, text="Add to Team 2", command=self.add_to_team2)
        self.teamb_button.pack()

        self.points_label = tk.Label(root, text="Press the 'Add Point' button or say 'Add point to team one' or 'Add point to team two'")
        self.points_label.pack()

        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.teama_p = 0
        self.teamb_p = 0

    def add_to_team1(self):
        self.teama_p += 1
        self.update_points_label()

    def add_to_team2(self):
        self.teamb_p += 1
        self.update_points_label()

    def update_points_label(self):
        self.points_label.config(text=f"Team {self.teama_entry.get()} has {self.teama_p} points. Team {self.teamb_entry.get()} has {self.teamb_p} points.")
        self.speak_points()

    def speak_points(self):
        message = f"Team {self.teama_entry.get()} has {self.teama_p} points. Team {self.teamb_entry.get()} has {self.teamb_p} points."
        self.engine.say(message)
        self.engine.runAndWait()

    def listen_mic(self):
        with sr.Microphone() as source:
            self.mic_button.config(text="Listening...")
            self.mic_button.update()
            audio = self.r.listen(source)

        try:
            command = self.r.recognize_google(audio)
            if "team one" in command:
                self.teama_p += 1
                self.update_points_label()
            elif "team two" in command:
                self.teamb_p += 1
                self.update_points_label()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TeamScoreTracker(root)
    root.mainloop()