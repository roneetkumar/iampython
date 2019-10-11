 # Assignment 1

# Write a program that requests a number from the keyboard,
# then prints out its binary representation and avoid printing leading zeros. (4 % ) - done
# Obviously, we did it in class with a format string, but that is not allowed for this assignment.
# The program should cater for numbers up to 65535. i.e. (2 ** 16) - 1
# Hint: you will need integer division (//), and modulo ( % ) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
# Once the program is working, modify it to print Octal rather than binary. (1 % ) - done


# what is input ?
# decimal number

# what is output ?
# a binary number

# algo to solve the problem ?
# check if num is smaller than equal to 0
# then return 0
# else
#
# pattern -
# 12 % 2 + 10 * (12 // 2)
# 0 + 10 * bin = 110
# 6 % 2 + 10 * (6 // 2)
# 0 + 10 * bin = 11
# 3 % 2 + 10 * (3 // 2)
# 1 + 10 * bin = 1
# 1 % 2 + 10 * (1 // 2)
# 1 + 10 * bin = 0
#
# return num % 2 + 10 * toBinary(num // 2)

# def toBinary(num):
#     if (num <= 0):
#         return 0
#     return num % 2 + 10 * toBinary(num // 2)

# def toOctal(num):
#     if (num <= 0):
#         return 0
#     return num % 8 + 10 * toBinary(num // 8)


def toBinary(num):
    return 0 if num <= 0 else num % 2 + 10 * toBinary(num // 2)


def toOctal(num):
    return 0 if num <= 0 else num % 8 + 10 * toBinary(num // 8)


while True:
    num = int(input("Enter a decimal number : "))
    if num < 65535:
        break

print(f"Converted into binary : {toBinary(num)}")
print(f"Converted into octal : {toOctal(num)}")
