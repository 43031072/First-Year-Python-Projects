import re
'''age = 20
price = 19.32
first_name = "Dbayne"
is_good = False'''
#name = input("What is your name? ")
#print("Hey: " + name)
#int()
#float()
#bool()
#str()
#if condition:
#   statement
#elif condition:
#   statement
#else:
#   statement
#while condition:
#   statement
#   increments
'''birth_date = input("Enter your name: ")
age = 2020 - int(birth_date)
print(age)'''

print("=======================================================================")
print("Users details")
userName = input("Enter your name: ")
surName = input("Enter your surname: ")
userEmail = input("Enter your email(e.g @gmail.com, @yahoo.com): ")
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', userEmail)
if valid:
    print("")
else:
    print("Invalid email!!")
phoneNumber = input("Enter your phone number(e.g 0123456789): ")
print("=======================================================================\n")

print("********************************************************")
print("Users Information:")
print("Name: " + userName)
print("Surname: "+ surName)
print("Email address: " + userEmail)
print("Phone Number: " + phoneNumber)
print("********************************************************")

