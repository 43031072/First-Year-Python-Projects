'''Mafora KM
43031072

This code is  using for loop to print negative integer from negative until zero '''
'''#requesting the user to input negative integer for the program
integer = int(input("Enter a negative integer : "))
#this condition warn the user about the restriction of the code
if integer > 0:
   print("The integer must be negative")
printing the numbers
for i in range(integer,1):
        print(i,end=" ")

theSum = 0
for count in range(1, 100001):
	theSum += count
print(theSum)

theSum = 0
while True:
    Data = input("Enter a number or just press enter to quit: ")
    if Data == "":
        break
    number = float(Data)
    theSum += number
print("The sum is",theSum)

while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 100 and 0")
print(number) # Just echo the valid input

five main numbers from 1 to 50 and one PowerBall from 1 to 20.
import random
for roll in range(5):
    print(random.randint(1,50),end=" ")'''
from math import*

while True:
    x1 = float(input("Enter the x-coordinate for point1: "))
    y1 = float(input("Enter the y-coordinate for point1: "))
    x2 = float(input("Enter the x-coordinate for ponit2: "))
    y2 = float(input("Enter the y-coordinate for point2: "))
    d = sqrt((x2-x1)**2+(y2-y1)**2)
    print("\nThe distance between point1 and point2 is:",d)
    radius = float(input("The radius of the circle is: "))
    circum = 2*pi*radius
    sur_area = pi*radius**2
    print("The circumference of the circle is: ",circum)
    print("The area of the circle is: ",sur_area)
    termination = input("Do you want to stop the program? (Yes/No): ")
    if termination == Yes:
        break
    else:
        continue





















