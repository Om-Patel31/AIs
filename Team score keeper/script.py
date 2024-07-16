import tkinter as tk
from tkinter import messagebox

class BadmintonScoreKeeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Badminton Scorekeeper")
        
        self.players = {}
        self.game_type = tk.StringVar(value="singles")
        self.score = {"Player1": 0, "Player2": 0, "Player3": 0, "Player4": 0}
        
        self.setup_ui()
        
    def setup_ui(self):
        tk.Label(self.root, text="Select Game Type:").pack()
        tk.Radiobutton(self.root, text="Singles", variable=self.game_type, value="singles", command=self.setup_game).pack()
        tk.Radiobutton(self.root, text="Doubles", variable=self.game_type, value="doubles", command=self.setup_game).pack()
        
        self.court_frame = tk.Frame(self.root)
        self.court_frame.pack()
        
        self.setup_game()
        
    def setup_game(self):
        for widget in self.court_frame.winfo_children():
            widget.destroy()
            
        if self.game_type.get() == "singles":
            self.players = {"Player1": "Player 1", "Player2": "Player 2"}
        else:
            self.players = {"Player1": "Player 1", "Player2": "Player 2", "Player3": "Player 3", "Player4": "Player 4"}
        
        self.score = {player: 0 for player in self.players}
        
        self.display_court()
        
    def display_court(self):
        self.court_canvas = tk.Canvas(self.court_frame, width=600, height=300, bg="green")
        self.court_canvas.pack()
        
        # Draw court boundaries
        self.court_canvas.create_rectangle(50, 50, 550, 250, outline="white", width=2)
        # Draw middle line
        self.court_canvas.create_line(300, 50, 300, 250, fill="white", dash=(5, 2))
        # Draw short service lines
        self.court_canvas.create_line(50, 150, 550, 150, fill="white", dash=(5, 2))
        # Draw left and right service courts
        self.court_canvas.create_line(175, 50, 175, 250, fill="white", dash=(5, 2))
        self.court_canvas.create_line(425, 50, 425, 250, fill="white", dash=(5, 2))
        
        self.shuttle = self.court_canvas.create_oval(285, 135, 315, 165, fill="white")
        
        self.score_labels = {}
        for player in self.players:
            self.score_labels[player] = tk.Label(self.court_frame, text=f"{self.players[player]}: {self.score[player]}")
            self.score_labels[player].pack()
        
        self.server_label = tk.Label(self.court_frame, text="Server: Player 1")
        self.server_label.pack()
        
        for player in self.players:
            tk.Button(self.court_frame, text=f"Add Point to {self.players[player]}", command=lambda p=player: self.add_point(p)).pack()
        
    def add_point(self, player):
        self.score[player] += 1
        for player_key in self.score_labels:
            self.score_labels[player_key].config(text=f"{self.players[player_key]}: {self.score[player_key]}")
        
        self.update_server()
        
    def update_server(self):
        if self.game_type.get() == "singles":
            server = "Player1" if (self.score["Player1"] + self.score["Player2"]) % 2 == 0 else "Player2"
        else:
            total_points = sum(self.score.values())
            if total_points % 4 == 0:
                server = "Player1"
            elif total_points % 4 == 1:
                server = "Player2"
            elif total_points % 4 == 2:
                server = "Player3"
            else:
                server = "Player4"
                
        self.server_label.config(text=f"Server: {self.players[server]}")
        
        # Move shuttle
        x_positions = {
            "Player1": 150, "Player2": 450, 
            "Player3": 150, "Player4": 450
        }
        y_position = 100 if (self.score[server] % 2 == 0) else 200
        
        if server in x_positions:
            self.court_canvas.coords(self.shuttle, x_positions[server] - 15, y_position - 15, x_positions[server] + 15, y_position + 15)

if __name__ == "__main__":
    root = tk.Tk()
    app = BadmintonScoreKeeper(root)
    root.mainloop()