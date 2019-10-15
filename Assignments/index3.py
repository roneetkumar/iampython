
def inputNum(str):
    '''
    INPUT : a string which program needs to print in order to prompt user to enter some value.\n
    OUTPUT : a INTEGER number value.\n
    DESC : if input is not a number the program prompt the user again to enter the value.
    '''

    while True:
        num = input(str)
        if not num.isdigit():
            continue
        break
    return int(num)


def displayMenu():
    '''
P - Print numbers\n
A - Add a number\n
M - Display mean of the numbers\n
S - Display the smallest number\n
L - Display the largest number\n
F - number to search in the list\n
Q - Quit
    '''

    print('''
P - Print numbers
A - Add a number
M - Display mean of the numbers
S - Display the smallest number
L - Display the largest number
F - number to search in the list
Q - Quit\n\n''')


def inputChar(str):
    '''
    INPUT:  a string which program needs to print in order to prompt user to enter some char.\n
    OUTPUT: one of these - 'p', 'a', 'm', 's', 'l', 'f', 'q'\n
    '''
    while True:
        choice = input(str)
        if (choice.lower() not in ['p', 'a', 'm', 's', 'l', 'f', 'q']):
            print("Unknown selection, please try again")
            continue
        break
    return choice


def displayNumbers(numbers):
    '''
    INPUT: list of numbers\n
    OUTPUT: dislpay all number in [] brackets with space
    '''
    print("[", end="")
    print(*numbers, end="")
    print("]", end="")


def findMean(numbers):
    '''
    INPUT: list of numbers\n
    OUTPUT: mean or average of all the numbers in the list
    '''
    return sum(numbers) / len(numbers)


def findMax(numbers):
    '''
    INPUT: list of numbers\n
    OUTPUT: largest number in the list
    '''
    Max = 0
    for num in numbers:
        if num > Max:
            Max = num
    return Max


def findMin(numbers):
    '''
    INPUT: list of numbers\n
    OUTPUT: smallest number in the list
    '''
    Min = numbers[len(numbers) - 1]
    for num in numbers:
        if num < Min:
            Min = num
    return Min


numbers = [2, 4, 4, 5, 10, 4, 5, 9]

displayMenu()

choice = inputChar("Enter your choice: ")

if choice == 'p':
    if not numbers:
        print("[] - the list is empty")
    else:
        displayNumbers(numbers)

elif choice == 'a':
    num = inputNum("Enter an integer to add to the list: ")
    numbers.append(num)
    print(f"{num} added")

elif choice == 'm':
    if not numbers:
        print("Unable to calculate the mean - no data")
    else:
        mean = findMean(numbers)
        print(mean)

elif choice == 's':
    if not numbers:
        print("Unable to determine the smallest number - list is empty")
    else:
        small = findMin(numbers)
        print(f"The smallest number is {small}")

elif choice == 'l':
    if not numbers:
        print("Unable to determine the largest number - list is empty")
    else:
        large = findMax(numbers)
        print(f"The largest number is {large}")

elif choice == 'f':
    if not numbers:
        print("cannot search - list is empty")
    else:
        num = inputNum("Enter a number to search in the list: ")
        if num in numbers:
            print(f"{num} occured {numbers.count(num)} time in the list")

else:
    print("Goodbye")
