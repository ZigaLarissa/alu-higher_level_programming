#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = str(number)
if x[-1] > 5:
    print(f"Last digit of {x} is {x[-1]} and is greater than 5")
elif x[-1] == 0:
    print(f"Last digit of {x} is {x[-1]} and is 0")
elif x[-1] < 6 and x[-1] != 0:
    print(f"Last digit of {x} is {x[-1]} and is less than 6 and not 0")
