# # 1. Write a program that reads 3 integers from the command line and assigns the read values to variables a, b, and c.

# num1 = int(input("Enter Num 1 : "))
# num2 = int(input("Enter Num 2 : "))
# num3 = int(input("Enter Num 3 : "))

# print(num1, num2, num3)

# if num1 > num2 > num3 or num1 < num2 < num3:
#     print(True)
# else:
#     print(False)

# # Write an expression inorder that evaluates to True if the numbers are either in ascending or descending order, and


# # False otherwise.
# # 2. Write a program spring.py that takes two integers m and d from the command line and writes True if day d of month
# # m is between March 21 and June 20, and False otherwise.

# d = int(input("Enter the day : "))
# m = input("Enter the month : ")


# if m.lower() == "march" and (d > 21 and d < 30):
#     print(True)
# elif m.lower() == "june" and (d > 1 and d < 20):
#     print(True)
# else:
#     print(False)


# # 3. Write a program squares.py with a for loop that produces the following output:
# # 1 4 9 16 25 36 49 64 81 100

# for num in range(1, 11):
#     print(num * num)


# 4. Write a program grid.py that prints an m x n grid of numbers in column major order. An example of a 5x6 grid is
# shown below. Hint: the value in the (i,j) location can be computed as i+mj
# 0 5 10 15 20 25
# 1 6 11 16 21 26
# 2 7 12 17 22 27
# 3 8 13 18 23 28
# 4 9 14 19 24 29

grid = []

for row in range(5):
    grid.append([])
    for col in range(6):
        grid[row].append(row + col * 5)

for x in grid:
    print(x)


# 5. Write a function substring(s1, s2, k) that takes two strings and an integer index k, and returns True if the first string

def substring(s1, s2, k):
    if s1.lower() in s2[k:].lower():
        print(True, s1)
    else:
        print(False)


substring('LOW', 'hellow', 3)

# appears as a substring in the second starting at location k. and False otherwise. Assume all strings are lowercase.
# 6. A. Write a function strings2float(ls) that takes a list of strings ls and returns a list of floats. Your function should
# construct the list of floats to return, and not modify the list passed in.


nums = [-2, -4, -34, -34, -2, -42]
pnums = []

for i in nums:
    if i > 0:
        pnums.append(i)

mini = pnums[0]

for i in range(len(pnums)):
    if pnums[i] < mini:
        mini = pnums[i]

print(mini)

# B. Write a function positive_min(lf) that returns the smallest positive float in the list lf

# C. Write a program minipos.py that reads a list of floats from the command line and prints the smallest positive
# value.
# > python minipos.py 4.5 -2.1 -8.2 3.5 7.5
# positive minimum is 3.5
# 7. Create a list (in one line) to return the multiplication table for an integer entered by the user. For example, if the user
# enters 5 then the output should be:
# [5, 1, 5]
# [5, 2, 10]
# [5, 3, 15]
# .
# .
# .
# [5, 10, 50]
# Hint: the list is a list of lists
# 8. Write a function flatten that returns a simple list containing all the values in a nested list. For example,
# flatten([2,9,[2,1,13,2],8,[2,6]]) returns [2,9,2,1,13,2,8,2,6]
