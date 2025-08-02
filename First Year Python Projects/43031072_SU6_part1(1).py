'''Mafora KM 43031072
A program that determine the area, volume and diagonal ofa a cuboid that has
width, length and height given by the user'''

from math import*
print("Cuboid calculator")# printing the heading for the program

#This part request the user to enter data to calculate 
width = float(input("\nEnter the width (cm): "))
length = float(input("Enter the length (cm): "))
height = float(input("Enter the height (cm): "))
#equations to be used to find answers
Area = 2*(length*width+length*height+width*height)
Volume = round((length*width*height),2)
Diagonal = sqrt(length**2+width**2+height**2)

#showing the user the results in detail
print("\nArea of the cuboid is %.4f"%Area,"square cm")
print(f"Space diagonal of the cuboid is ",Diagonal,"cm")
print(f"Volume of the cuboid is%.2f "%Volume,"cubic cm")
print("\n***Cunoid dimension:**")
print(f"width =",width,"cm \t length = ",length,"cm \t height =",height,"cm")
