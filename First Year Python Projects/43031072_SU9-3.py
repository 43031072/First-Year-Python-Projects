'''Mafora KM
43031072
This code asks the user to enter his/her particulars (student number and name, comma
delimited) and stores it in a variable student_info. It initializes two variables
student_number and student_name to store the extracted student number and name. Then
it loops through the characters in student_info using a for loop and checks if the
current character is a comma. If it is, it extracts the student number and name using
array indexing and slicing and breaks out of the loop. Finally, it prints out the
student number and name as output.'''

# Asking the user to enter his/her particulars(student number and name, comma delimited)
student_info = input("Enter your student number and name, separated by a comma: ")

# Initialize variables to store the student number and name
student_number = ""
student_name = ""

# Loop through the characters in the information
for i in range(len(student_info)):
    # Check if the current character is a comma
    if student_info[i] == ",":
        # Extract the student number and name using array indexing and slicing
        student_number = student_info[:i].strip()
        student_name = student_info[i+1:].strip()
        break

# Print out the student number and name as output
print(f"Student Number: {student_number}")
print(f"Student Name: {student_name}")
