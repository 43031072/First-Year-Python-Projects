'''Mafora KM
43031072
This code asks the user to enter an integer value greater than 1 and validates
the input using a while loop. If the input is invalid, it asks the user to enter
a valid value until a valid entry is made. Then it displays the multiplication
table from 1 to 5 for the entered value using a for loop.'''

# Ask the user to enter an integer value greater than 1
num = int(input("Enter an integer value greater than 1: "))

# Input validation using a while loop
while num <= 1:
    print("Invalid input! the value must be greater than 1.")
    num = int(input("Enter an integer value greater than 1: "))

# Showing  the multiplication table based on the user-input
for i in range(1, 6):
    print(f"{num} x {i} = {num * i}")
