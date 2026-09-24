# Two-Room Vacuum Cleaner

room = {
    "A": "Dirty",
    "B": "Dirty"
}

position = "A"


while True:
    print("\nCurrent Position:", position)
    print("Room A:", room["A"])
    print("Room B:", room["B"])

    # If current room is dirty, clean it
    if room[position] == "Dirty":
        print("Action: Suck")
        room[position] = "Clean"

    # If current room is clean, move to the other room
    else:
        if position == "A":
            print("Action: Move Right")
            position = "B"
        else:
            print("Action: Move Left")
            position = "A"

    # Stop when both rooms are clean
    if room["A"] == "Clean" and room["B"] == "Clean":
        print("\nBoth rooms are clean!")
        break
