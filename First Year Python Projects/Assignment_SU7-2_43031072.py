#Mafora KM
#43031072
#Date: 05/05/2023

#asking the user to enter two number and an operater ( +,-,*,/) to perform mathematical operations

Number1 = float(input("Enter the first number: "))
Number2 = float(input("Enter the second number: "))
Operator = str(input("Enter the operator(+,-,*,/): "))
Error_Operators = ["+","-","*","/"]

#printing the users choice of options
if Operator not in Error_Operators:
    print("Invalid operator")
elif Operator == "+":
    print(Number1 + Number2)
elif Operator == "-":
    print(Number1 - Number2)
elif Operator == "*":
    print(Number1 * Number2)
elif Operator == "/":
    if Number2 == 0:
        print("Error : Division by 0 !!")
    else:
            print(Number1 / Number2)



