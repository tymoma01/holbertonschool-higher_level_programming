#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = (abs(number) % 10) * -1 
else:
    last_digit = abs(number) % 10

if last_digit % 10 > 5:
    suffix = "greater than 5"
if last_digit % 10 == 0:
    suffix = "0"
elif last_digit % 10 < 6:
    suffix = "less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} and is {suffix}")