#Kesaobaka Mafora 43031072

#Coding convertion from character to its ASCII values and vise versa
print("**ASCII and Character conversion**\n")#Title
Character = input("Enter character: ")#requesting the user to input character

ASCII_value = ord(Character)#finding the ASCII value
print(f"the ASCII value is: {ASCII_value}\n")#printing the value
value = int(input("Enter the ASCII value: "))#requesting user to input a value
Character = chr(value)#finding the character
print(f"The character is : {Character}")#printing character
