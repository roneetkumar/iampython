locations = {
    0: "You are sleeping",
    1: "You are walking on a road",
    2: "You are at the top of a hill",
    3: "You are inside a building",
    4: "You are in a valley",
    5: "You are in the forest"
}

exits = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}
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
