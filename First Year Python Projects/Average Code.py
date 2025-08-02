print("Welcome to a system that calculate averages of different thing from the number of your family members\n")
print("**************************************************************************************************")
print("\n__________________________Instructions__________________________")

print("\n1.Please provide accurate information to accumulate accurate results")
print("2.You will have to provide only number of family members so that the code can function proparly")
print("3.Please do not enter things that you are not required to enter\n")

print("**************************************************************************************************\n")

NumMem = int(input("Enter the amount of your family members. e.g 1- 20: "))
Sisters = int(input("How many sisters do you have: "))
Brothers = int(input("How many brothers do you have: "))
Matric = int(input("Enter the number of members who finished matric: "))
LeftSchool = int(input("Enter the number of members with no matric: "))
Unemployed = int(input("Enter the number of members who are unemployed: "))
Employed = int(input("Enter the number of members who are employed: "))

choice = str(input("\n\nDo you want to continue with calculations('yes'/'no'. NB: write your choice in small letters): "))

while(choice == 'yes'):
    print("\n1.Average of Sisters vs brothers: ")
    print("2.Average of members who made it to matric vs those who did not: ")
    print("3.Average of members who are unemployed vs those who are employed: ")
    print("4.Average of all things mentioned above: ")

    decision = int(input("\nEnter any number from above to get answer: "))

    if(decision == 1):
        AveSisters = float((Sisters*100)/NumMem)
        AveBrothers = float((Brothers*100)/NumMem)

        print("\n______________ Sisters Vs Brothers ______________")
        print("The average is ",AveSisters, " Vs ", AveBrothers)
        
    elif(decision == 2):
        AveMatric = float((Matric*100)/NumMem)
        AveLeftSchool = float((LeftSchool*100)/NumMem)

        print("\n______________ with Matric Vs without matric ______________")
        print("The average is",AveMatric, " Vs ", AveLeftSchool)

    elif(decision == 3):
        AveUnemployed = float((Unemployed*100)/NumMem)
        AveEmployed = float((Employed*100)/NumMem)

        print("\n______________ Unemployed Vs Employed ______________")
        print("The average is",AveUnemployed, " Vs ", AveEmployed)
        
    elif(decision == 4):
        AveSisters = float((Sisters*100)/NumMem)
        AveBrothers = float((Brothers*100)/NumMem)

        print("\n______________ Sisters Vs Brothers ______________")
        print("The average is ",AveSisters, " Vs ", AveBrothers)

        AveMatric = float((Matric*100)/NumMem)
        AveLeftSchool = float((LeftSchool*100)/NumMem)

        print("\n______________ with Matric Vs without matric ______________")
        print("The average is",AveMatric, " Vs ", AveLeftSchool)

        AveUnemployed = float((Unemployed*100)/NumMem)
        AveEmployed = float((Employed*100)/NumMem)

        print("\n______________ Unemployed Vs Employed ______________")
        print("The average is",AveUnemployed, " Vs ", AveEmployed)
    
    else:
        break
