
def compareTriplets(a, b):
    ali = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            print("alis")
            ali += 1
        elif a[i] < b[i]:
            print("bob")
            bob += 1
        else:
            print("pass")
            pass

    return [ali, bob]


a = [2, 6, 5]

b = [3, 6, 2]

result = compareTriplets(a, b)

print(result)
