

# def sq(num):
#     return num**2


list = [1, 2, 3, 4]

# for i in map(sq, list):
#     print(i)


for i in filter(lambda num:  num % 2 == 0, list):
    print(i)
