#Mafora KM
#43031072
#Date: 05/05/2023

#Python code that prompts the user to enter their age and whether they have their ID card with them

Age = int(input("Enter your age : "))
ID_Status = input("Enter your ID status (Y/N): ")
#Checking whether the infomation correspond with the rules
if (Age >=18):
    if (ID_Status == "Y"):
        print("You are eligible to buy alcohol")
    elif (ID_Status == "N"):
        print("Invalid status")
else:
    print("You are not eligible to buy alcohol")
