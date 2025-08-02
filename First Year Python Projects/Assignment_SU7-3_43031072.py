#Mafora KM
#43031072
#Date: 05/05/2023

#Importing math module for mathematical operation

from math import*

# request the user to enter base and the expornent
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent number: "))

#Code conditions to be met by users choice

if exponent < 0 :
    print("Error : exponent cannot be negative")
elif (base == 0) and (exponent == 0):
    print("Error: indeterminate form (0^0)")
else:
    results = pow(base,exponent)
    print(f"{base} to the power of {exponent} is: {results}")
