'''Mafora KM 43031072
python script that promots the user to enter a base and an exponent to
evaluate and give feedback to the user'''
from math import*
#Asking the user to enter values
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
#finding the results for the user's choice with strict conditions
if base == 0 and exponent ==0:
    print("Error: Indeterminate form(0^0)")
elif exponent < 0:
    print("Error:exponent cannot be negative")
else:
    print(base**exponent)
