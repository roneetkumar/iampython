# print all the options
# get the choice from the user
# if not correct choice ask again with while loop

# execute the appropriate option based on user choice with if elif else conditional statements


def runProgram():
    numbers = [2, 4, 4, 5, 10, 4, 5, 9]
    print('''
P - Print numbers
A - Add a number
M - Display mean of the numbers
S - Display the smallest number
L - Display the largest number
F - number to search in the list
Q - Quit\n\n''')

    while True:
        choice = input("Enter your choice: ")
        if (choice.lower() not in ['p', 'a', 'm', 's', 'l', 'f', 'q']):
            print("Unknown selection, please try again")
            continue
        break

    if choice == 'p':
        if not numbers:
            print("[] - the list is empty")
        else:
            print("[", end="")
            print(*numbers, end="")
            print("]", end="")
        runProgram()
    elif choice == 'a':
        while True:
            num = input("Enter an integer to add to the list: ")
            if not num.isdigit():
                continue
            num = int(num)
            break
        numbers.append(num)
        print(f"{num} added")

    elif choice == 'm':
        if not numbers:
            print("Unable to calculate the mean - no data")
        else:
            print(sum(numbers) / len(numbers))

        runProgram()
    elif choice == 's':
        if not numbers:
            print("Unable to determine the smallest number - list is empty")
        else:
            print(f"The smallest number is {min(numbers)}")
        runProgram()
    elif choice == 'l':
        if not numbers:
            print("Unable to determine the largest number - list is empty")
        else:
            print(f"The largest number is {max(numbers)}")
        runProgram()
    elif choice == 'f':
        if not numbers:
            print("cannot search - list is empty")
        else:
            while True:
                num = input("Enter a number to search in the list: ")
                if not num.isdigit():
                    continue
                num = int(num)
                break
        if num in numbers:
            print(f"{num} occured {numbers.count(num)} time in the list")
        runProgram()
    else:
        print("Goodbye")


runProgram()
