# A.Write a function strings2float(ls) that takes a list of strings ls and
#  returns a list of floats. Your function should construct the list of floats to return,
#  and not modify the list passed in.


def string2float(ls):
    '''
    INPUT: list of string numbers as (ls)\n
    OUTPUT: return list of floats\n
    DESC:
    '''
    newLs = []
    for i in ls:
        newLs.append(float(i))
    return newLs


stringLS = ['1', '2', '3', '4', '5']

print(string2float(stringLS))


# B. Write a function positive_min(lf)
#  that returns the smallest positive float in the list lf


def positive_min(ls):
    '''
    INPUT: list of float numbers as (ls)\n
    OUTPUT: return the smallest positive value\n
    DESC:
    '''
    min = ls[0]
    for num in ls:
        if num > 0 and num < min:
            min = num
    return min


floatList = [1.32, 5.4, 8.7, -3.2, -6.0]

print(positive_min(floatList))


# C.
#  Write a program minipos.py that reads a list of floats from the command
# line and prints the smallest positive value.

# > python minipos.py 4.5 - 2.1 - 8.2 3.5 7.5 positive minimum is 3.5

def readNums(str):
    while True:
        try:
            num = float(input(str))
            break
        except:
            print("Enter a valid integer")
            continue
    return float(num)


def minipos():
    numOfItems = int(readNums("Enter no. of value : "))
    list = []
    for i in range(numOfItems):
        num = readNums(f"Enter a number {i+1} : ")
        list.append(num)
    print(list)
    print(positive_min(list))


minipos()

# Create a list(in one line) to return the multiplication table
# for an integer entered by the user. For example, if the user enters 5
# then the output should be:  [5, 1, 5][5, 2, 10][5, 3, 15] . . . [5, 10, 50]


def table(num):
    for i in range(10):
        print(f"[{num}, {i+1}, {num*(i+1)}] ", end="")


table(4)
