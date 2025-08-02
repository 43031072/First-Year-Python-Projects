#Kesaobaka Mafora 43031072

#For x1

print("Solving ax^2 + bx + c =0")#Title

a = int(input("Enter the value of a: "))#User's value for a
b = int(input("Enter the value of b: "))#User's value for b
c = int(input("Enter the value of c: "))#User's value for c
from math import*

#Equations to be used to provide answers
y = (b**2) - (4*a*c)
x1 = (-b + sqrt(y) )/(2*a)
x2 = (-b-2 + sqrt(y) )/(2*a)

print("\nROOTS OF GIVEN QUADRATIC EQUATIONS ARE: ")#Title
print("x1:",x1)#Solution for x1
print("x2:",x2)#Solution for x
