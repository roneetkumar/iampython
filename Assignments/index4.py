#  Write a program grid.py that prints an m x n grid of numbers in column major order.
#  An example of a 5x6 grid is shown below. Hint: the value in the(i, j) location can
#  be computed as i+mj 0 5 10 15 20 25 1 6 11 16 21 26 2 7 12 17 22 27 3 8 13 18 23 28 4 9 14 19 24 29


def grid(m, n):
    '''
    INPUT: (colmuns x rows) as (m , n) \n
    OUTPUT: prints the grid using for loop
    '''
    for i in range(m):
        for j in range(n):
            print(i + m * j, end="\t")
        print("\n\n\n", end="")


grid(5, 6)


# Write a function substring(s1, s2, k) that takes two strings and an integer index k,
# and returns True if the first string appears as a substring in the second starting at location k.
# and False otherwise. Assume all strings are lowercase

def substring(s1, s2, k):
    '''
    INPUT: (substring,full string, start location) as (s1,s2,k)\n
    OUTPUT: Boolean \n
    True if string found after start location\n
    False otherwise
    '''
    if s1.lower() in s2.lower()[k:]:
        print(True)
    else:
        print(False)


findStr = 'or'
fullString = 'hello world'
startLocation = 3

substring(findStr, fullString, startLocation)
