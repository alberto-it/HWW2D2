"""
1. Decisions at the Crossroad
Task 1: Code Correction
"""
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

print()
"""
2. The Greatest Showdown
Task 1: Identify the Greatest
Write a Python program that prompts the user to enter three numbers. 
The program should then identify and print out the largest number among the three.
"""
num1 = int(input("Enter first  number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third  number: "))

print("\n Biggest...")
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

"""
Task 2: Identify the Smallest
Extend your program from Task 1 to also determine the smallest number among the three and print it out.
"""    
print("\n Smallest...")
if num1 <= num2 and num1 <= num3:
    print(num1)
elif num2 <= num1 and num2 <= num3:
    print(num2)
else:
    print(num3)

"""
Task 3: Equality Check
Enhance your program to handle cases where two or all of the numbers are equal. 
The program should display appropriate messages like 
"Two numbers are equal and the largest" or "All numbers are equal".

Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that 
"The smallest number is 3. The largest number is 4. There are two numbers equal to each other."
Printing out which numbers are equal would be a great added bonus.
"""
print("\n Equality Check... \n")
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("The smallest number is",smallest)
print("The largest  number is", largest)

if num1 == num2 and num1 == num2 and num2 == num3:
    print("All numbers are equal")
else:
    if num1 == num2:
        print("There are two numbers equal to each other (first and second numbers)")
        if num1 == smallest:
            print("and is the smallest")
        if num1 == largest:
            print("and is the largest")
    if num1 == num3:
        print("There are two numbers equal to each other (first and third numbers)")
        if num1 == smallest:
            print("and is the smallest")
        if num1 == largest:
            print("and is the largest")
    if num2 == num3:
        print("There are two numbers equal to each other (second and third numbers)")
        if num2 == smallest:
            print("and is the smallest")
        if num2 == largest:
            print("and is the largest")

print()

"""
3. Leap Year Explorer
Task 1: Leap Year Checker
Every year that is exactly divisible by four is a leap year, 
except for years that are exactly divisible by 100, 
but these centurial years are leap years if they are exactly divisible by 400.

Expected Outcome: If you test the year 1900, is should be False. 
The year 2000 should be True. The year 2024 should be True
"""
year = int(input("Enter Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        print(year % 400 == 0) #returns True or False
    else:
        print(True)
else:
    print(False)

print()
