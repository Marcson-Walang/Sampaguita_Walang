# Long Test Part 3
# Marcson Dojan A. Walang  8 -  Sampaguita    9/30/2026

import re
import string

valid_activity = ["robotics", "coding", "science", "arts"]

name = input("Enter your name: ")
age = int(input("Enter your age: "))
activity = (input("Enter your activity: ").lower())

s1 = 1
s2 = 1
s3 = 1

if name.strip():
    s1 = 1
else :
    s1 = 2

if  0 <= age <= 100:
    s2 = 1
else :
    s2 = 2

    if activity in valid_activity:
        s3 = 1
    else :
        s3 = 2

if s1 == 1 and s2 == 1 and s3 == 1 :
    print("Registration Successful")
elif s1 == 2 and s2 == 1 and s3 == 1 :
    print("Enter Your Name")
elif s1 == 1 and s2 == 2 and s3 == 1 :
    print("Invalid Age")
elif s1 == 1 and s2 == 1 and s3 == 2 :
    print("Invalid Activity")
