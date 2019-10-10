import math

# STRINGS
# str = "Hello World"
# print(str)

# -----------------------------------------------


# STRING FORMATING
# print(f"{str} " * 5)

# -----------------------------------------------


# BEFORE MUTATION
# price = 10
# print(price)


# -----------------------------------------------


# AFTER MUTATION
# price = 20
# print(price)

# -----------------------------------------------


# BOOLEANS
# is_reading = True

# -----------------------------------------------


# pName = input("Enter Your Name : ")
# print(f"Hi {pName}!")

# -----------------------------------------------


# TYPE CASTING
# birth_year = input("Enter Your Age : ")
# age = 2019 - int(birth_year)
# print(age)

# -----------------------------------------------


# MULTILINE SRTING
# str = '''
# Hello sir,
# How are you doing
# '''

# -----------------------------------------------


# print(str)
# course = "Python Course for Beginners"
# course = course[::-1]
# print(course)

# -----------------------------------------------


# print(4 + 3)
# print(4 - 3)
# print(4 * 3)
# print(4 / 3)
# print(4 % 3)
# print(4 // 3)

# -----------------------------------------------


# i = 0
# while i < 10:
#     print(i)
#     i = i+1

# -----------------------------------------------


# num = 9

# guess_count = 0
# while guess_count < 3:
#     guess = int(input("Guess : "))
#     guess_count += 1
#     if guess == num:
#         print("win")
#         break
# else:
#     print("fail")

# -----------------------------------------------


# command = ''
# started = False

# while True:
#     command = input("> ").lower()
#     if command == 'start':
#         if started:
#             print("started already")
#         else:
#             started = True
#             print("started")
#     elif command == 'stop':
#         if not started:
#             print("already stoped")
#         else:
#             started = False
#             print("stoped")
#     elif command == 'help':
#         print('''
# start
# stop
# quit
#         ''')
#     elif command == 'quit':
#         break
#     else:
#         print("sorry")


# -----------------------------------------------


# for items in range(10):
#     print(items)


# for items in range(1, 10):
#     print(items)


# for items in range(10, -10, -1):
#     print(items)


# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price

# print(f"Total is : {total}")


# -----------------------------------------------

# number = [1, 1, 1, 1, 5]

# for x in number:
#     output = ''
#     for y in range(x):
#         output += 'x'
#     print(output)


# numbers = [12, 3, 5, 5, 6, 7, 1]
# max = numbers[0]
# for num in numbers:
#     if num > max:
#         max = num

# print(max)


# -----------------------------------------------


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# for row in matrix:
#     for item in row:
#         print(item)

# -----------------------------------------------


# numbers = [5, 5, 6, 4, 3, 6, 8]

# numbers.append(20)

# print(numbers)

# numbers.insert(0, 20)

# print(numbers)

# numbers.insert(len(numbers)//2, 20)

# print(numbers)

# numbers.pop()

# print(numbers)

# print(numbers.index(3))

# print(numbers.count(20))

# print(20 in numbers)

# numbers.sort()

# numbers.reverse()

# print(numbers)

# -----------------------------------------------


# uniques = []
# for num in numbers:
#     if num not in uniques:
#         uniques.append(num)

# print(uniques)

# -----------------------------------------------


# numbers = (1, 2, 4)

# x, y, z = numbers

# print(x, y, z)

# -----------------------------------------------


# def table(num):
#     for i in range(10):
#         i += 1
#         print(f"{num} * {i} = {num*i}")


# table(7)

# -----------------------------------------------


# array = [10][10]

# for i in range(10):
#     print('')
#     for j in range(10):
#         if i == j or i + j == 9:
#             print("   ", end='')
#         else:
#             print("0 ", end='')


# -----------------------------------------------


# customer = {
#     "name": "john smith",
#     "age": 30,
#     "is_verified": True
# }

# print(customer["name"])
# print(customer.get("name"))

# print(customer)

# -----------------------------------------------


# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))


# res = num1/num2 if num1 == num2 else num1 if num1 > num2 else num2

# if num1 == num2:
#     res = num1 / num2
# else:
#     if num1 > num2:
#         res = num1
#     else:
#         res = num2

# print(res)


# -----------------------------------------------


# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError as err:
#     print("Invalid Error")


# -----------------------------------------------


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point = Point()

# print(point.x)


# -----------------------------------------------

# MODULES

# from Animal import dog, cat

# dog.bark()
# cat.meow()

# -----------------------------------------------


# from package1 import fucntions

# numbers = [2, 4, 22, -6, 1, 9, 3, 10]

# maximum = fucntions.find_min(numbers)

# print(maximum)

# -----------------------------------------------


# numbers = [1, 3, 5, 7, 9]
# pairList = []

# for i in numbers:
#     for j in numbers:
#         if i % j == 0:
#             pairList += [[i, j]]

# print(pairList)

# -----------------------------------------------


# from random import randint


# class Dice:
#     def roll(self):
#         return (randint(1, 6), randint(1, 6))


# dice = Dice()

# print(dice.roll())

# -----------------------------------------------


# from pathlib import Path

# path = Path("hello")

# # print(path.glob('*.py'))

# for file in path.glob('*.py'):
#     print(file)

# print('end')

# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference

# wb = xl.load_workbook("trans.xlsx")

# sheet = wb['Sheet1']

# for row in range(2, sheet.max_row + 1):
#     cell = sheet.cell(row, 3)
#     final = cell.value * 3
#     final_cell = sheet.cell(row, 4)
#     final_cell.value = final

# values = Reference(sheet,
#                    min_row=2,
#                    max_row=sheet.max_row,
#                    min_col=4,
#                    max_col=4
#                    )


# chart = BarChart()
# chart.add_data(values)

# sheet.add_chart(chart, 'e2')

# wb.save('newTrans.xlsx')
