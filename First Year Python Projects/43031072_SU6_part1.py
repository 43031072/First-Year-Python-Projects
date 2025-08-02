#Kesaobaka Mafora 43031072
from math import*

print("Cone calculator")#Title

#Requesting the user to assign any value
Radius = int(input("\nEnter the radius (cm): "))
Height = int(input("Enter the height (cm): "))

#Equations to be used to provide answers
Area = pi * Radius *( Radius + sqrt((Height ** 2 ) + (Radius ** 2)))
Volume = (pi * Radius ** 2 * Height) /3
diagonal = sqrt((Radius ** 2) + (Height ** 2 ))

print("\nArea of the cone is %.4f"%Area,"square cm")#printing statement about area of cone
print("Space diagonal of the cone is %.3f"%diagonal,"cm")#printing statement about diagonal of cone
print("Volume of the cone is %.2f"%Volume,"cubic cm")#printing statement about volume of cone
print("\n**Cone dimention:**")#printing heading
print(f"radius = {float(Radius)} cm \theight = {float(Height)} cm")
