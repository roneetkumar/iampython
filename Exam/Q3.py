def checkAnimals():
    heads = input("Total Heads: ")
    legs = input("Total Legs : ")
    print(f"No. of heads: {heads} and no. of legs: {legs}")

    var = (int(legs) - 2 * int(heads))
    ans = var / 2

    if not (var % 2 == 0):
        print("not possible. try again.")
        checkAnimals()
    else:
        print("Number of Lions (with 4 legs)  are: " + str(int(ans)))
        print(
            f"Number of Kangaroos with 2 legs of  are: {int(int(heads) - ans)}")


checkAnimals()
