# pro = {(1, 2): "qq",
#    "q": "qqq"}


# pro["q"] = "rr"

# pro.clear()


pro = {
    "apple": "ghjkl",
    "mango": "gvhbjnk",
    "grape": "fcgvhjk"
}

i = input("enter")

if i in pro:
    print(f"value of {i} is {pro[i]}")
else:
    print(f"{i} is not in the list")
