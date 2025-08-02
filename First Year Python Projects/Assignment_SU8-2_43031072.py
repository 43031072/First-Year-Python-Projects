'''Mafora KM
43031072

This code if using while loop to print negative integer starting from zero
and at the ent if combine the total of the integers
#Requesting the user to enter a negative integer
integer = int(input("Enter a negative integer: "))

i = 0
#using the while loop to find the values of the user
while i > integer:
    print(i,end=" ")
    i -= 1
sum_integer = sum(range(integer,-0))
for i in range(1,integer):
    print(i,end=" ")
#printing the users integer and the totalof the combinition
print(integer,"=",sum_integer)

for i in range(0,5):
    print("*" * i)


    
for i in range(0,5):
    print("*" * 5)



for i in range(1,5):
    print("*" * 5)'''


for count in range(5):
      print(count + 1, end=" ")
