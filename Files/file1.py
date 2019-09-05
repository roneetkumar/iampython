from datetime import datetime
import time
import random

odds = []

for i in range(0, 60):
    if i % 2 != 0:
        odds.append(i)

currentMinute = datetime.today().minute

for i in range(5):
    if currentMinute in odds:
        print("this minute is bit odd")
    else:
        print("Not an odd minute")
    print(currentMinute)
    time.sleep(random.randrange(1, 60))
