locations = {
    0: "Your are sleepig",
    1: "You are on road",
    2: "You are in school",
    3: "You are in building",
    4: "You are in restaurant",
    5: "You are in forest",
    6: "You are in ocean",
    7: "You are in hell",
    8: "You are in paradise",
}

exits = {
    0: {"Q": 0},
    1: {"N": 5, "S": 4, "E": 3, "W": 2, "Q": 0},
    2: {"N": 7, "Q": 0},
    3: {"E": 1, "Q": 0},
    4: {"N": 1, "W": 8, "E": 6, "Q": 0},
    5: {"W": 5, "S": 1, "Q": 0},
    6: {"W": 4, "Q": 0},
    7: {"S": 2, "E": 5, "Q": 0},
    8: {"N": 2, "E": 4, "Q": 0},
}

words = {
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
    "QUIT": "Q"
}

loc = 1

while True:
    availableExits = ""

    for i in words:
        if words[i] in exits[loc].keys():
            availableExits += f", {i}"

    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are " + availableExits + " ").upper()

    for i in words:
        if direction == i:
            direction = words[i]

    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
