import math

Number1 = int(input("Enter the first number: "))
Number2 = int(input("Enter the second number: "))
No3 = 1
No4 = 1

def calulate_sum():
    global No3
    No3 = Number1 + Number2
    print(f"Sum: {No3} ")
def calculate_difference():
    global No4
    No4 = Number1 - Number2
    print(f"Difference: {No4}")
calulate_sum()
calculate_difference()