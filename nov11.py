

with open('./new.txt', 'w') as city:
    for n in range(1, 13):
        print(f"{2} times {n} is {n*2}", file=city)
