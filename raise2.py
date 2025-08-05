'''c=int(input("Enter temperature in c: "))
f=(c*9/5)+32
assert(f<=32), "Its cold"
print("Fahrenheit:" ,f)'''

'''Write a program which infinitely prints natural numbers . raise a stopIteration exception when the number is greater than 20.'''
'''def display(n):
    while True:
        try:
            n+=1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n , end=" ")
i=0
display(i)'''

'''import random
class RandomError(Exception):
    pass
try:
    num.random.random()
    if num<0.1:
        raise RandomError
except RandomError as e:
    print("RandomError generated")
else:
    print("No error generated")'''

'''import calendar
Year = int(input("Enter year: "))
Month = int(input("Enter month: "))
str=calendar.month(Year,Month)
print(str)'''

'''import calendar
year = int(input("Enter year: "))
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'''

'''Program to print the next 10 days dates continuously from today.'''

'''from datetime import *
d=date.today()
print(d)
d=date(1966,6,29)
for x in range(10):
    nextdate = d + timedelta(days=x)
    print(nextdate)'''

'''import time
epoch = time.time()
print(epoch)'''

import sys
if len(sys.argv) <2:
    print("Usage: hello hi.py <name>")
else:
    name= sys.argv[1]
    print(f"student, {name}!")
