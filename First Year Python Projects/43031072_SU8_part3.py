'''Mafora KM 43031072
python script that promots the user to enter a base and an exponent to
evaluate and give feedback to the user'''
from math import*
while True:
    #Welcoming the user warmly and requesting the user to input all the values needed for calculations
    user_name = input("Enter your name: ")
    print("Warm greetings ",user_name)
    radius = int(input("Enter the radius(cm): "))
    length = int(input("Enter the length(cm): "))
    width = int(input("Enter the width(cm): "))
    side1 = int(input("Enter the side(cm): "))
    side2 = int(input("Enter the side(cm): "))
    side3 = int(input("Enter the side(cm): "))
    #Equations to be used to calculate the perimeter
    Circle_Perimeter  = 2*pi*radius
    triangle_Perimeter = side1+side2+side3
    square_Perimeter = 4*side1
    rectangle_Perimeter = 2*(length + width)
    #print the results of the user
    print("The perimeter of circle is",Circle_Perimeter,"cm")
    print("The perimeter of the triangle is",triangle_Perimeter,"cm")
    print("The perimeter of a square is",square_Perimeter,"cm")
    print("The perimeter of rectangle is",rectangle_Perimeter,"cm")
    #termination of the code by the user's own choice
    stop_continue =input("\nIf you will like to continue enter 'continue' and if you will like to stop enter 'stop'")
    if stop_continue == ("continue"):
        continue
    elif stop_continue == "stop":
        break
