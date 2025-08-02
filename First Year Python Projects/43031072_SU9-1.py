'''43031072
Mafora KM

This code is used to check if people have access to use enter the private properties for work.
The user must have their id card with them for the machine to scan and
allow access or deny access to the user'''
#first the information like name and ID number is collected from the user
while True:
    list_1 = []
    ID_Scanning = int(input("\nEnter your ID number: "))
#This is the list of people who have access to the private property
    ID_list = list([10203040,93245683,92857611,19284538,10293857,57483920,48024601])
#Conditions to be considered during the process
    if ID_Scanning not in ID_list:
        print("Access denied, for more information contact the owner's PR")
    else:
        print("Welcome, attend meeting before working.")
        list_1.append(ID_list)
        print("\nScan ID to continue")
#The user must choose if they want to scan their ID or not so that the machine can work
    Scanning = input("\nEnter Scan to continue: ")
    if Scanning == 'Scan':
        continue
    else:
        break
#A loop of the employees
for i in range(1,8):
        print(i," Employee ")


    

