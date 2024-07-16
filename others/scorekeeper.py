import keyboard

print("Press the (+) key to add points.")

teama = input("Enter the name of team 1:")
teama_p = 0
teamb = input("Enter the name of team 2:")
teamb_p = 0

def on_key_event(event):
    global teama_p, teamb_p
    if event.name == 'plus':
        pointt = input("Which team do I add the point to (Enter the name of the team):")
        if pointt == teama:
            teama_p += 1
            print("Team", teama, "has", teama_p, "points. Team", teamb, "has", teamb_p, "points.")
        elif pointt == teamb:
            teamb_p += 1
            print("Team", teama, "has", teama_p, "points. Team", teamb, "has", teamb_p, "points.")

keyboard.on_press_key('plus', on_key_event)

# Keep the program running
keyboard.wait('esc')